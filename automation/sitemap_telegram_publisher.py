#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sitemap-Driven Telegram Channel Publisher for Aividia (aividia.ir)
Platform: GitHub Actions / Automated Scheduler
Frequency: 4 times daily (09:00 to 21:00 IRST)

Tracks all previous and newly published blog posts in the live sitemap.
Selects exactly one unannounced post per run (4 runs/day), extracts core value
and reader benefits, and publishes a persuasive community-shareable Telegram post.
"""

import os
import sys
import re
import json
import time
import urllib.parse
from datetime import datetime
import xml.etree.ElementTree as ET
import requests

# Configure UTF-8 encoding for Windows / CI
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
if not BOT_TOKEN or not CHAT_ID:
    print("❌ Error: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID environment variables must be set.")
    sys.exit(1)

TRACKER_PATH = os.path.join("telegram channel", "sitemap_posts_tracker.json")
SITEMAP_URL = "https://aividia.ir/post-sitemap.xml"

HTTP_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 (AividiaBot/2.0)'
}

EXCLUDED_SLUGS = [
    'hello-world',
    'sample-page',
    'cart',
    'checkout',
    'my-account'
]

def normalize_url(u):
    """Normalize URLs for reliable dictionary matching across percent-encoded & unicode strings."""
    if not u:
        return ""
    clean = u.strip().rstrip('/')
    return urllib.parse.unquote(clean)

def fetch_live_sitemap_urls():
    """Fetch all blog post URLs and lastmod timestamps from the live XML sitemap."""
    try:
        resp = requests.get(SITEMAP_URL, headers=HTTP_HEADERS, timeout=20)
        if resp.status_code != 200:
            print(f"⚠️ Sitemap fetch failed with status: {resp.status_code}")
            return []
        
        root = ET.fromstring(resp.content)
        ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        results = []
        for url_elem in root.findall('sm:url', ns):
            loc_elem = url_elem.find('sm:loc', ns)
            lastmod_elem = url_elem.find('sm:lastmod', ns)
            
            if loc_elem is not None and loc_elem.text:
                loc = loc_elem.text.strip()
                lastmod = lastmod_elem.text.strip() if (lastmod_elem is not None and lastmod_elem.text) else ""
                
                # Exclude administrative or non-article slugs
                if any(ex in loc for ex in EXCLUDED_SLUGS):
                    continue
                    
                results.append({
                    "url": loc,
                    "lastmod": lastmod
                })
        
        # Sort descending by lastmod (newest articles first)
        results.sort(key=lambda x: x.get("lastmod", ""), reverse=True)
        return results
    except Exception as e:
        print(f"❌ Error fetching sitemap: {e}")
        return []

def load_tracker():
    """Load or initialize the tracker file."""
    if os.path.exists(TRACKER_PATH):
        try:
            with open(TRACKER_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"published_urls": {}, "history": []}

def save_tracker(tracker):
    """Save updated tracker state."""
    os.makedirs(os.path.dirname(TRACKER_PATH), exist_ok=True)
    with open(TRACKER_PATH, "w", encoding="utf-8") as f:
        json.dump(tracker, f, ensure_ascii=False, indent=2)

def extract_article_meta(url):
    """Extract title, description, og:image, and key subtopics from live article HTML."""
    try:
        r = requests.get(url, headers=HTTP_HEADERS, timeout=20)
        if r.status_code != 200:
            print(f"⚠️ Failed to fetch article at {url} (HTTP {r.status_code})")
            return None
        
        html = r.text
        
        # 1. Title
        m_title = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        raw_title = m_title.group(1).strip() if m_title else ""
        clean_title = re.sub(r'[\s–|-]+(?:آیویدیا|Aividia|پلتفرم سلامت).*$', '', raw_title, flags=re.IGNORECASE).strip()
        if not clean_title:
            clean_title = raw_title
            
        # 2. Meta Description (with intelligent paragraph fallback for older posts)
        m_desc = re.search(r'<meta[^>]*name=[\'"]description[\'"][^>]*content=[\'"](.*?)[\'"]', html, re.IGNORECASE)
        if not m_desc:
            m_desc = re.search(r'<meta[^>]*content=[\'"](.*?)[\'"][^>]*name=[\'"]description[\'"]', html, re.IGNORECASE)
        desc = m_desc.group(1).strip() if m_desc else ""
        
        if not desc or len(desc) < 30:
            # Fallback: extract first substantive paragraph from body
            paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', html, re.IGNORECASE | re.DOTALL)
            for p in paragraphs:
                clean_p = re.sub(r'<[^>]+>', '', p).strip()
                if len(clean_p) > 60 and not any(skip in clean_p for skip in ['کوکی', 'جاوااسکریپت', 'مرورگر']):
                    desc = clean_p[:180] + '...'
                    break
        
        # 3. OG Image (Featured Image with in-body fallback)
        m_og_img = re.search(r'<meta[^>]*property=[\'"]og:image[\'"][^>]*content=[\'"](.*?)[\'"]', html, re.IGNORECASE)
        og_img = m_og_img.group(1).strip() if m_og_img else ""
        
        if not og_img:
            m_img = re.search(r'<img[^>]+src=[\'"]([^\'"]+uploads[^\'"]+)[\'"]', html, re.IGNORECASE)
            if m_img:
                og_img = m_img.group(1)
        
        # 4. H2 Headings (Key benefits / subtopics)
        h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.IGNORECASE | re.DOTALL)
        h2_clean = []
        for h in h2s:
            cleaned = re.sub(r'<[^>]+>', '', h).strip()
            # Skip generic headings
            if cleaned and not any(skip in cleaned for skip in ['سوالات متداول', 'نتیجه‌گیری', 'منابع', 'دیدگاه‌ها', 'مقدمه']):
                h2_clean.append(cleaned)
                
        return {
            "url": url,
            "title": clean_title,
            "desc": desc,
            "og_image": og_img,
            "key_points": h2_clean[:3]
        }
    except Exception as e:
        print(f"❌ Error scraping article {url}: {e}")
        return None

def compose_telegram_post(meta):
    """
    Format a high-engagement Persian Telegram post designed to persuade readers
    and encourage community forwarding.
    """
    title = meta["title"]
    url = meta["url"]
    desc = meta.get("desc", "")
    points = meta.get("key_points", [])
    
    # Contextual category & tool detection
    tool_cta = ""
    category_emoji = "📌"
    
    url_lower = url.lower()
    if any(k in url_lower for k in ['spartina', 'mounjaro', 'ozempic', 'لاغری', 'تیرزپاتاید', 'glp']):
        category_emoji = "💉"
        tool_cta = "🔹 <b>ارزیابی رایگان شرایط داروی لاغری:</b>\n👉 <a href='https://aividia.ir/glp1-need-assessment/'>تست آنلاین واجد شرایط بودن مانجارو و اسپارتینا</a>\n"
    elif any(k in url_lower for k in ['routine', 'روتین', 'پوست-چرب', 'پوست-خشک']):
        category_emoji = "✨"
        tool_cta = "🔹 <b>آنالیزور ۱۰ مرحله‌ای روتین پوست (رایگان):</b>\n👉 <a href='https://aividia.ir/skin-routine-analyzer/'>تست آنلاین نوع پوست و دریافت روتین شخصی</a>\n"
    elif any(k in url_lower for k in ['scabies', 'گال', 'اگزما', 'قارچ', 'fungal', 'cancer', 'سرطان']):
        category_emoji = "🔬"
        tool_cta = "🔹 <b>تریاژ و غربالگری ضایعات پوستی با هوش مصنوعی:</b>\n👉 <a href='https://aividia.ir/'>اسکن آنلاین بیماری‌های پوستی با مدل ۷۲۴ آیویدیا</a>\n"
    else:
        category_emoji = "🩺"
        tool_cta = "🔹 <b>ویزیت آنلاین فوری پزشک عمومی:</b>\n👉 <a href='https://aividia.ir/shop/%d9%88%db%8c%d8%b2%db%8c%d8%aa-%d8%a2%d9%86%d9%84%d8%a7%db%8c%d9%86-%d9%be%d8%b2%d8%b4%da%a9-%d8%b9%d9%85%d9%88%d9%85%db%8c-%d9%86%d8%b3%d8%ae%d9%87-%d9%81%d9%88%d8%b1%db%8c/'>دریافت نسخه فوری و مشاوره آنلاین</a>\n"

    # Format Key Points
    points_text = ""
    if points:
        points_text = "<b>💡 آن‌چه در این مقاله تخصصی یاد می‌گیرید:</b>\n"
        for p in points[:3]:
            clean_p = p.split('(')[0].split(':')[0].split('؛')[0].strip()
            points_text += f"▫️ {clean_p}\n"
        points_text += "\n"

    tracking_url = f"{url}?utm_source=telegram&utm_medium=channel&utm_campaign=sitemap_autopost"

    desc_block = f"📝 <i>{desc}</i>\n\n" if desc else ""

    caption = (
        f"{category_emoji} <b>{title}</b>\n\n"
        f"{desc_block}"
        f"{points_text}"
        f"🔗 <b>مطالعه کامل مقاله در وب‌سایت آیویدیا:</b>\n"
        f"👉 <a href='{tracking_url}'>کلیک کنید و متن کامل مقاله را بخوانید</a>\n\n"
        f"{tool_cta}\n"
        f"📤 <i>این راهنما را برای دوستان و گروه‌هایی که با این موضوع مواجه هستند فوروارد کنید تا از راهکارهای علمی آن بهره‌مند شوند.</i>\n\n"
        f"🩺 <b>پلتفرم سلامت و هوش مصنوعی آیویدیا</b>\n"
        f"🆔 @aividia_test | 🌐 <a href='https://aividia.ir/'>aividia.ir</a>"
    )

    return caption

def send_telegram_post(text, photo_url=None):
    """Send photo with caption (clamped to 1024 chars) or fall back to rich HTML message."""
    if photo_url:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        
        # Clamp caption safely to <= 1020 chars
        caption = text
        if len(caption) > 1020:
            caption = caption[:1015] + "..."
            
        payload = {
            "chat_id": CHAT_ID,
            "photo": photo_url,
            "caption": caption,
            "parse_mode": "HTML"
        }
        res = requests.post(url, json=payload, timeout=30)
        data = res.json()
        if data.get("ok"):
            return data
        print(f"⚠️ Failed sendPhoto: {data.get('description')}. Falling back to sendMessage...")

    # Fallback to sendMessage (supports up to 4096 chars and web page preview)
    msg_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    res = requests.post(msg_url, json=payload, timeout=20)
    return res.json()

def main():
    dry_run = "--dry-run" in sys.argv
    force_url = None
    if "--url" in sys.argv:
        idx = sys.argv.index("--url")
        if idx + 1 < len(sys.argv):
            force_url = sys.argv[idx + 1]

    print("=" * 60)
    print("🚀 AIVIDIA SITEMAP BLOG POST TELEGRAM PUBLISHER")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 60)

    tracker = load_tracker()
    published_urls = tracker.get("published_urls", {})
    normalized_published = {normalize_url(k): v for k, v in published_urls.items()}

    target_entry = None

    if force_url:
        print(f"🎯 Force mode: Targeting URL: {force_url}")
        target_entry = {"url": force_url, "lastmod": datetime.now().isoformat()}
    else:
        print(f"📡 Fetching live sitemap: {SITEMAP_URL}...")
        sitemap_items = fetch_live_sitemap_urls()
        total_sitemap_count = len(sitemap_items)
        print(f"✅ Found {total_sitemap_count} total blog articles in sitemap.")

        # Identify all unannounced articles (both previous and newly published)
        unannounced = [item for item in sitemap_items if normalize_url(item["url"]) not in normalized_published]
        announced_count = total_sitemap_count - len(unannounced)
        print(f"📊 Sitemap Status: {announced_count} already announced | {len(unannounced)} pending in queue.")

        if unannounced:
            # Pick the next article in chronological order (freshest first)
            target_entry = unannounced[0]
            print(f"✨ Selected Next Article: {target_entry['url']} (Lastmod: {target_entry.get('lastmod')})")
        else:
            print("ℹ️ All sitemap articles have been announced! Selecting least-recently posted evergreen guide to rotate...")
            sorted_published = sorted(sitemap_items, key=lambda x: published_urls.get(x["url"], {}).get("published_at", ""))
            if sorted_published:
                target_entry = sorted_published[0]
                print(f"🔄 Rotating evergreen guide: {target_entry['url']}")

    if not target_entry:
        print("❌ No article available to publish.")
        sys.exit(0)

    url = target_entry["url"]
    print(f"\n🔍 Extracting metadata from live page: {url}...")
    meta = extract_article_meta(url)

    if not meta:
        print(f"❌ Could not extract metadata from {url}. Aborting.")
        sys.exit(1)

    print(f"📄 Title: {meta['title']}")
    print(f"🖼️ Featured Image: {meta['og_image']}")
    print(f"💡 Key Subtopics: {len(meta['key_points'])} extracted")

    post_content = compose_telegram_post(meta)

    if dry_run:
        print("\n" + "-" * 40)
        print("🔍 [DRY RUN PREVIEW]:")
        print("-" * 40)
        print(post_content)
        print("-" * 40)
        print("✅ Dry run completed successfully. No message sent to Telegram.")
        return

    print("\n📤 Dispatching to Telegram channel...")
    res = send_telegram_post(post_content, photo_url=meta.get("og_image"))

    if res.get("ok"):
        msg_id = res["result"]["message_id"]
        print(f"🎉 SUCCESS! Published to Telegram with Message ID: {msg_id}")

        # Update tracker
        now_str = datetime.now().isoformat()
        tracker["published_urls"][url] = {
            "title": meta["title"],
            "published_at": now_str,
            "lastmod": target_entry.get("lastmod", ""),
            "telegram_message_id": msg_id
        }
        tracker.setdefault("history", []).append({
            "url": url,
            "title": meta["title"],
            "published_at": now_str,
            "message_id": msg_id
        })

        save_tracker(tracker)
        print(f"💾 Updated {TRACKER_PATH} with publication record for message #{msg_id}.")
    else:
        print(f"❌ Telegram API Error: {res}")
        sys.exit(1)

if __name__ == "__main__":
    main()
