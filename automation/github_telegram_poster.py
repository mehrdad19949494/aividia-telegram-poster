import os
import sys
import json
import requests
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
if not BOT_TOKEN or not CHAT_ID:
    print("❌ Error: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID environment variables must be set.")
    sys.exit(1)

DB_PATH = os.path.join("telegram channel", "posts_database.json")

def send_telegram_message(text, parse_mode="HTML", disable_web_page_preview=False):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": disable_web_page_preview
    }
    response = requests.post(url, json=payload, timeout=20)
    return response.json()

def send_telegram_photo(photo_url_or_path, caption="", parse_mode="HTML"):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHAT_ID,
        "caption": caption,
        "parse_mode": parse_mode
    }
    
    if os.path.exists(photo_url_or_path):
        with open(photo_url_or_path, 'rb') as img_file:
            files = {'photo': img_file}
            response = requests.post(url, data=payload, files=files, timeout=30)
    else:
        payload["photo"] = photo_url_or_path
        response = requests.post(url, json=payload, timeout=20)
        
    return response.json()

def main():
    dry_run = "--dry-run" in sys.argv
    test_single = "--test-single" in sys.argv

    if not os.path.exists(DB_PATH):
        print(f"❌ Database file not found at: {DB_PATH}")
        sys.exit(1)

    with open(DB_PATH, "r", encoding="utf-8") as f:
        posts = json.load(f)

    # Auto-replenish if pending queue is empty or low (< 20)
    pending_posts = [p for p in posts if p.get("status") == "pending"]
    if len(pending_posts) < 20:
        print(f"🔄 Pending queue low ({len(pending_posts)} < 20). Triggering auto-replenishment...")
        try:
            from automation.replenish_posts import replenish
        except ImportError:
            try:
                from replenish_posts import replenish
            except ImportError:
                replenish = None
        if replenish:
            replenish()
            with open(DB_PATH, "r", encoding="utf-8") as f:
                posts = json.load(f)
            pending_posts = [p for p in posts if p.get("status") == "pending"]

    if not pending_posts:
        print("⚠️ No pending posts found in database even after replenishment check!")
        sys.exit(0)

    target_post = pending_posts[0]
    print(f"📌 Selected Post #{target_post['id']} - [{target_post['pillar']}] {target_post['title']}")

    if dry_run:
        print("🔍 [DRY RUN] Post content preview:\n")
        print(f"Has Photo: {target_post.get('has_photo')} (Path: {target_post.get('photo_url')})")
        print(target_post["text"])
        print("\n✅ Dry run finished. No changes saved.")
        return

    # Deliver post to Telegram
    if target_post.get("has_photo") and target_post.get("photo_url"):
        photo_path = target_post["photo_url"]
        caption = target_post["text"]
        # Telegram caption max length is 1024 characters
        if len(caption) > 1020:
            caption = caption[:1017] + "..."
        print(f"🚀 Sending photo post #{target_post['id']} to Telegram (File: {photo_path})...")
        res = send_telegram_photo(photo_path, caption=caption)
    else:
        print(f"🚀 Sending text post #{target_post['id']} to Telegram...")
        res = send_telegram_message(target_post["text"])

    if res.get("ok"):
        msg_id = res["result"]["message_id"]
        print(f"✅ Published successfully! Telegram Message ID: {msg_id}")
        
        # Update post status
        target_post["status"] = "published"
        target_post["published_at"] = datetime.now().isoformat()
        target_post["telegram_message_id"] = msg_id

        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)

        print(f"💾 Updated {DB_PATH} with published status for post #{target_post['id']}.")
    else:
        print(f"❌ Failed to publish post: {res.get('description')}")
        sys.exit(1)

if __name__ == "__main__":
    main()

