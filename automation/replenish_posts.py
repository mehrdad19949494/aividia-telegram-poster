import os
import sys
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = os.path.join("telegram channel", "posts_database.json")

# Verified Canonical Live URLs
URL_SKIN_AI = "https://aividia.ir/"
URL_ONLINE_GP = "https://aividia.ir/shop/%d9%88%db%8c%d8%b2%db%8c%d8%aa-%d8%a2%d9%86%d9%84%d8%a7%db%8c%d9%86-%d9%be%d8%b2%d8%b4%da%a9-%d8%b9%d9%85%d9%88%d9%85%db%8c-%d9%86%d8%b3%d8%ae%d9%87-%d9%81%d9%88%d8%b1%db%8c/"
URL_SKIN_CANCER = "https://aividia.ir/"
URL_ROUTINE_ANALYZER = "https://aividia.ir/skin-routine-analyzer/"
URL_GLP1_DOCTOR_SUITE = "https://aividia.ir/glp1-prescribing-assistant-2/"
URL_GLP1_B2C_ASSESSMENT = "https://aividia.ir/glp1-need-assessment/"

FORWARD_PROMPT = "📤 <i>این مطلب کاربردی را برای عزیزانی که به سلامت پوست و بهداشت خود اهمیت می‌دهند بفرستید.</i>"
CHANNEL_SIGNATURE = "🆔 @aividia_test"

# 50 Distinct Structured Posts (5 Full Days x 10 Daily Slots)
POSTS_CATALOG = [
    # ==================== DAY 1 (Posts 1-10) ====================
    {
        "slot_time": "08:00",
        "pillar": "Morning Health Tip",
        "service_target": "Model 724 Skin AI",
        "title": "خارش بین انگشتان و مچ دست؛ تفاوت گال با اگزمای دیس‌هایدروتیک",
        "lines": [
            "خارش شدید شبانه بین انگشتان دست می‌تواند اولین علامت بیماری گال باشد.",
            "اما اگر وزیکول‌ها (تاول‌های ریز شفاف) همراه با سوزش ظاهر شوند، احتمال اگزمای دیس‌هایدروتیک مطرح است.",
            "تشخیص زودهنگام مانع از انتقال بیماری در خانواده می‌شود."
        ],
        "cta": "آنالیز آنلاین نوع ضایعه پوستی با هوش مصنوعی آیویدیا",
        "url": URL_SKIN_AI,
        "has_photo": True,
        "photo_url": "telegram channel/images/infographic_scabies_vs_eczema.jpg"
    },
    {
        "slot_time": "09:30",
        "pillar": "AI Case Study",
        "service_target": "Model 724 Skin AI",
        "title": "بررسی کیس واقعی: افتراق درماتیت سبورئیک از پسوریازیس کف سر با هوش مصنوعی",
        "lines": [
            "بیمار ۲۸ ساله با پوسته‌ریزی ضخیم و قرمزی شدید در حاشیه رویش مو مراجعه کرد.",
            "مدل ۷۲۴ آیویدیا با دقت بالینی احتمال ۹۱٪ درماتیت سبورئیک مقاوم را در مقایسه با پلاک‌های پسوریازیس تشخیص داد.",
            "بر اساس گزارش تحلیلی، پروتکل شامپو کتوکونازول و قطره لوسیون تجویز شد."
        ],
        "cta": "آپلود تصویر و دریافت گزارش تحلیلی هوش مصنوعی",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "11:00",
        "pillar": "Skin Routine Guide",
        "service_target": "Skin Routine Analyzer",
        "title": "۳ گام ضروری برای ترمیم سد دفاعی پوست آسیب‌دیده (Skin Barrier)",
        "lines": [
            "۱. شوینده بسیار ملایم با pH متعادل (۵.۵) بدون ایجاد احساس کشیدگی.",
            "۲. آبرسانی عمیق با هیالورونیک اسید و پانتنول (B5).",
            "۳. قفل‌کردن رطوبت با کرم‌های حاوی سرامید، کلسترول و اسیدهای چرب ضروری."
        ],
        "cta": "دریافت برنامه روتین اختصاصی پوست شما (رایگان)",
        "url": URL_ROUTINE_ANALYZER,
        "has_photo": True,
        "photo_url": "telegram channel/images/infographic_skin_barrier.jpg"
    },
    {
        "slot_time": "12:30",
        "pillar": "Interactive Quiz",
        "service_target": "Model 724 Skin AI",
        "title": "تست خودسنجی: آیا پوست شما دهیدراته است یا چرب؟",
        "lines": [
            "آیا بعد از شستشو روی پیشانی و بینی براق است ولی گونه‌ها احساس خشکی و سوزش دارند؟",
            "این وضعیت نشان‌دهنده «پوست دهیدراته چرب» است که نیاز به آبرسان بدون چربی (Oil-Free) دارد نه لایه‌بردار خشن!"
        ],
        "cta": "تست آنلاین و شناسایی نوع دقیق پوست",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "14:00",
        "pillar": "GLP-1 Weight Management",
        "service_target": "B2B GLP-1 Prescribing Suite (Doctors)",
        "title": "رونمایی از دستیار بالینی هوشمند تجویز داروهای GLP-1 (مونجارو و اوزمپیک) ویژه پزشکان",
        "lines": [
            "پلتفرم تخصصی تصمیم‌یار بالینی آیویدیا برای پزشکان عمومی، متخصصین غدد و کلینیک‌های لاغری:",
            "🔹 محاسبه‌گر گام‌به‌گام نردبان دوزبندی ۶ داروی چاقی (تیرزپاتاید/مونجارو، سماگلوتاید/اوزمپیک، ساکسندا، ویگووی، اسپارتینا، ریتاتروتاید).",
            "🔹 جدول هوشمند و داینامیک مدیریت ۱۷ عارضه شایع گوارشی با پروتکل‌های دارویی مکمل.",
            "🔹 تولید برگه استاندارد دو بخشی بیمار و رضایت‌آگاهی کتبی در فرمت A4 افقی جهت بایگانی مطب."
        ],
        "cta": "ورود به سوئیت بالینی تصمیم‌یار تجویز GLP-1 پزشکان (نسخه ۱.۲)",
        "url": URL_GLP1_DOCTOR_SUITE,
        "has_photo": True,
        "photo_url": "telegram channel/images/infographic_glp1_titration.jpg"
    },
    {
        "slot_time": "15:30",
        "pillar": "Melasma & Sun Protection",
        "service_target": "Model 724 Skin AI",
        "title": "ضدآفتاب مینرال (فیزیکی) یا کمیکال؟ کدام برای پوست‌های لک‌دار مناسب‌تر است؟",
        "lines": [
            "ضدآفتاب‌های مینرال حاوی زینک اکساید با مسدود کردن طیف کامل نور مرئی مانع از تحریک سلول‌های ملانوسیت در لک ملاسما می‌شوند.",
            "برای درمان لک‌های بارداری و آفتاب، همیشه ضدآفتاب تینت‌دار (رنگی) با زینک اکساید ترجیح داده می‌شود."
        ],
        "cta": "آنالیز شدت لک‌های صورت با هوش مصنوعی",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "17:00",
        "pillar": "Skin Cancer Prevention",
        "service_target": "Model 1066 Skin Cancer Screening",
        "title": "چک‌لیست طلایی ABCDE برای غربالگری و بررسی خال‌های مشکوک پوستی",
        "lines": [
            "خال‌های پوستی خود را بر اساس ۵ نشانه کلیدی بررسی کنید:",
            "A: عدم تقارن (Asymmetry) | B: لبه‌های ناصاف و دندانه‌دار (Border)",
            "C: تنوع رنگ چندگانه (Color) | D: قطر بزرگتر از ۶ میلی‌متر (Diameter)",
            "E: هرگونه تغییر در اندازه، خارش یا خونریزی (Evolving)"
        ],
        "cta": "غربالگری هوشمند احتمال بدخیمی خال با مدل ۱۰۶۶",
        "url": URL_SKIN_CANCER,
        "has_photo": True,
        "photo_url": "telegram channel/images/infographic_abcde_melanoma.jpg"
    },
    {
        "slot_time": "18:30",
        "pillar": "Interactive Quiz",
        "service_target": "Model 724 Skin AI",
        "title": "کوئیز پزشکی: آیا سوزش پوست بعد از کرم زدن طبیعی است؟",
        "lines": [
            "اگر هر نوع کرم مرطوب‌کننده عادی باعث سوزش پوست شما می‌شود، علت آن نازک شدن لایه اپیدرم و آسیب سد لیپیدی است.",
            "در این حالت باید موقتاً کلیه لایه‌بردارها و شوینده‌های صابونی را متوقف کنید."
        ],
        "cta": "تشخیص و ارزیابی آنلاین علائم پوستی",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "20:00",
        "pillar": "Online GP Spotlight",
        "service_target": "Online GP Doctor Visit",
        "title": "ویزیت آنلاین پزشک عمومی؛ دریافت نسخه الکترونیک معتبر بدون معطلی",
        "lines": [
            "نیاز به نسخه داروهای تجویزی، تمدید داروهای مزمن یا درخواست آزمایش‌های دوره‌ای دارید؟",
            "پزشکان عمومی آیویدیا پس از بررسی آنلاین شرح‌حال و علائم، نسخه معتبر الکترونیک تامین اجتماعی و سلامت را در سریع‌ترین زمان صادر می‌کنند."
        ],
        "cta": "درخواست ویزیت آنلاین پزشک عمومی (نسخه فوری)",
        "url": URL_ONLINE_GP,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "21:30",
        "pillar": "Evening Skincare Recap",
        "service_target": "Skin Routine Analyzer",
        "title": "ترتیب صحیح استفاده از محصولات روتین شب و روز (Layering Order)",
        "lines": [
            "قانون اصلی لایه‌بندی: از سبک‌ترین بافت (آبکی) به سنگین‌ترین بافت (کرمی):",
            "صبح: شوینده ملایم ⬅️ سرم ویتامین C ⬅️ مرطوب‌کننده ⬅️ ضدآفتاب SPF 50+",
            "شب: دابل کلینز ⬅️ اکتیوهای درمانی (رتینول یا BHA) ⬅️ کرم ترمیم‌کننده شب"
        ],
        "cta": "دریافت رایگان راهنمای روتین اختصاصی شما",
        "url": URL_ROUTINE_ANALYZER,
        "has_photo": True,
        "photo_url": "telegram channel/images/infographic_skincare_layering.jpg"
    },

    # ==================== DAY 2 (Posts 11-20) ====================
    {
        "slot_time": "08:00",
        "pillar": "Morning Health Tip",
        "service_target": "Model 724 Skin AI",
        "title": "علائم تبخال تناسلی و زگیل پوستی (HSV / HPV) و روش‌های تفکیک آن",
        "lines": [
            "ضایعات وزیکولی تاول‌دار دردناک معمولاً ناشی از ویروس تبخال (HSV) هستند.",
            "در حالی که ضایعات بدون درد گل‌کلمی اغلب نشان‌دهنده پاپیلوماویروس (HPV) می‌باشند.",
            "تشخیص زودهنگام کلید کنترل ویروس و پیشگیری از عوارض است."
        ],
        "cta": "آنالیز تصویری ضایعات مشکوک با هوش مصنوعی آیویدیا",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "09:30",
        "pillar": "AI Case Study",
        "service_target": "Model 724 Skin AI",
        "title": "کیس واقعی: تشخیص ریزش موی سکه‌ای (Alopecia Areata) در مراحل اولیه",
        "lines": [
            "بیمار ۳۱ ساله با لکه خالی دایره‌ای بدون التهاب در ریش و پوست سر مراجعه کرد.",
            "مدل ۷۲۴ ریزش موی خودایمنی سکه‌ای را تشخیص داده و ضرورت تزریق موضعی کورتیکواستروئید تحت نظر پزشک را توصیه نمود."
        ],
        "cta": "اسکن هوشمند الگوی ریزش مو با آیویدیا",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "11:00",
        "pillar": "Skin Routine Guide",
        "service_target": "Skin Routine Analyzer",
        "title": "چگونه اسید سالیسیلیک (BHA) را بدون لایه‌برداری بیش‌ازحد مصرف کنیم؟",
        "lines": [
            "اسید سالیسیلیک محلول در چربی است و مستقیماً وارد منافذ مسدود شده و جوش‌های سرسیاه می‌شود.",
            "استفاده را با ۱ تا ۲ شب در هفته آغاز کنید و هرگز همزمان با رتینول استفاده نکنید."
        ],
        "cta": "تحلیل تخصصی روتین ضد جوش پوست شما",
        "url": URL_ROUTINE_ANALYZER,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "12:30",
        "pillar": "Interactive Quiz",
        "service_target": "Model 724 Skin AI",
        "title": "تست: آیا لک‌های قهوه‌ای شما ملاسما است یا جای جوش (PIH)؟",
        "lines": [
            "لک‌های ملاسما متقارن و در اثر هورمون و آفتاب هستند، در حالی که لک PIH دقیقاً در محل جوش‌های قبلی ایجاد می‌شود.",
            "درمان این دو نوع لک نیازمند ترکیبات کاملاً متفاوتی است."
        ],
        "cta": "آنالیز آنلاین نوع لک صورت با هوش مصنوعی",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "14:00",
        "pillar": "GLP-1 Weight Management",
        "service_target": "B2C GLP-1 Need Assessment & Referral",
        "title": "آیا کاندید علمی استفاده از داروهای نوین لاغری (مونجارو/تیرزپاتاید) هستید؟",
        "lines": [
            "استپ وزنی، مقاومت به انسولین و شکست رژیم‌های مکرر اغلب منشا هورمونی دارند نه اراده ضعیف!",
            "سامانه ارزیابی هوشمند آیویدیا شاخص توده بدنی (BMI)، بیماری‌های همراه (کبد چرب، تخمدان پلی‌کیستیک، فشار خون) و فاکتورهای منع مصرف را در ۱ دقیقه تحلیل می‌کند.",
            "پس از تکمیل تست، نامه رسمی ارجاع به پزشک با گزارش بالینی کامل دریافت می‌کنید یا می‌توانید مستقیماً ویزیت آنلاین پزشک عمومی را رزرو نمایید."
        ],
        "cta": "شروع ارزیابی آنلاین بالینی نیاز به داروی لاغری و دریافت نامه ارجاع",
        "url": URL_GLP1_B2C_ASSESSMENT,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "15:30",
        "pillar": "Melasma & Sun Protection",
        "service_target": "Model 724 Skin AI",
        "title": "ترکیبات طلایی در درمان لک‌های مقاوم به درمان ملاسما",
        "lines": [
            "ترکیب ترانگزامیک اسید (موضعی یا خوراکی)، آزالائیک اسید ۲۰٪ و نیاسینامید ۴٪ طبق مقالات درماتولوژی بیشترین اثر را در مهار تولید ملانین دارند."
        ],
        "cta": "مشاوره آنلاین پوست و درمان لک با پزشک عمومی",
        "url": URL_ONLINE_GP,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "17:00",
        "pillar": "Skin Cancer Prevention",
        "service_target": "Model 1066 Skin Cancer Screening",
        "title": "کارسینوم سلول بازال (BCC)؛ شایع‌ترین سرطان پوست با چه علائمی بروز می‌کند؟",
        "lines": [
            "BCC معمولاً به شکل برجستگی مرواریدی، زخم با بهبودی دیرهنگام یا رگ‌های خونی ریز روی صورت نمایان می‌شود.",
            "تشخیص در مراحل اولیه امکان درمان ۱۰۰٪ قطعی را فراهم می‌کند."
        ],
        "cta": "اسکن و غربالگری هوشمند ضایعات پوستی مشکوک",
        "url": URL_SKIN_CANCER,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "18:30",
        "pillar": "Interactive Quiz",
        "service_target": "Model 724 Skin AI",
        "title": "کوئیز: آیا ناخن ضخیم و زرد شده شما قارچ ناخن (اونیکومایکوزیس) است؟",
        "lines": [
            "تغییر رنگ به زرد/قهوه‌ای، خرد شدن لبه ناخن و بوی نامطبوع از علائم اصلی عفونت قارچی ناخن است.",
            "برای درمان قطعی داروهای خوراکی ضدقارچ با نسخه پزشک الزامی است."
        ],
        "cta": "آنالیز آنلاین عفونت‌های ناخن با هوش مصنوعی",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "20:00",
        "pillar": "Online GP Spotlight",
        "service_target": "Online GP Doctor Visit",
        "title": "ویزیت آنلاین برای چکاپ کبد چرب، آزمایش‌های تیروئید و قند خون",
        "lines": [
            "اگر نیاز به بررسی آزمایش‌های دوره‌ای، آنزیم‌های کبدی یا تنظیم دوز داروها دارید، پزشکان آیویدیا با دقت بالینی پاسخگوی شما هستند."
        ],
        "cta": "ثبت درخواست ویزیت آنلاین پزشک عمومی",
        "url": URL_ONLINE_GP,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "21:30",
        "pillar": "Evening Skincare Recap",
        "service_target": "Skin Routine Analyzer",
        "title": "چک‌لیست سلامت پوست: ۵ اشتباه شبانه که باعث مسدود شدن منافذ می‌شود",
        "lines": [
            "۱. خوابیدن با ضدآفتاب یا آرایش ❌",
            "۲. نشستن بالش‌ها به صورت هفتگی ❌",
            "۳. استفاده از کرم‌های سنگین روغنی روی پوست چرب ❌",
            "۴. لایه‌برداری با اسکراب‌های زبر فیزیکی ❌",
            "۵. عدم استفاده از مرطوب‌کننده بعد از شستشو ❌"
        ],
        "cta": "دریافت روتین علمی و بهینه برای پوست شما",
        "url": URL_ROUTINE_ANALYZER,
        "has_photo": False,
        "photo_url": ""
    },

    # ==================== DAY 3 (Posts 21-30) ====================
    {
        "slot_time": "08:00",
        "pillar": "Morning Health Tip",
        "service_target": "Model 724 Skin AI",
        "title": "عفونت زردزخم (Impetigo) در کودکان؛ علائم تاول‌های عسلی‌رنگ",
        "lines": [
            "زردزخم یک عفونت باکتریایی شایع و بسیار مسری در کودکان است که با دلمه‌های عسلی‌رنگ دور دهان و بینی مشخص می‌شود.",
            "پماد موپیروسین موضعی یا آنتی‌بیوتیک خوراکی باید با تجویز پزشک شروع شود."
        ],
        "cta": "بررسی فوری ضایعات پوستی کودک با هوش مصنوعی",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "09:30",
        "pillar": "AI Case Study",
        "service_target": "Model 724 Skin AI",
        "title": "کیس واقعی: تفکیک آکنه روزاسه از آکنه ولگاریس با مدل ۷۲۴",
        "lines": [
            "بیمار ۳۹ ساله با قرمزی مداوم گونه‌ها و جوش‌های بدون کومدون سرسیاه مراجعه نمود.",
            "هوش مصنوعی با دقت بالا آکنه روزاسه اریتماتوتلانژکتازی را شناسایی کرد که درمان آن با آکنه عادی متفاوت است."
        ],
        "cta": "آنالیز اختصاصی قرمزی و جوش صورت با هوش مصنوعی",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "11:00",
        "pillar": "Skin Routine Guide",
        "service_target": "Skin Routine Analyzer",
        "title": "راهنمای کوچک‌کردن منافذ باز پوست (Enlarged Pores)",
        "lines": [
            "منافذ پوست عضله ندارند و باز و بسته نمی‌شوند، اما با پاکسازی چربی اضافه با نیاسینامید و سالیسیلیک اسید بسیار جمع‌تر و کوچک‌تر به نظر می‌رسند."
        ],
        "cta": "آنالیز تخصصی روتین جمع‌کننده منافذ",
        "url": URL_ROUTINE_ANALYZER,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "12:30",
        "pillar": "Interactive Quiz",
        "service_target": "Model 724 Skin AI",
        "title": "تست: آیا خارش پوست شما کهیر حاد است یا درماتیت تماسی؟",
        "lines": [
            "ضایعات برجسته قرمز که ظرف ۲۴ ساعت جا‌به‌جا می‌شوند نشان‌دهنده کهیر هستند.",
            "اما ضایعات ثابت همراه با پوسته در محل برخورد زیورآلات یا عطر نشانه درماتیت تماسی آلرژیک است."
        ],
        "cta": "تشخیص دقیق علت خارش با هوش مصنوعی آیویدیا",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "14:00",
        "pillar": "GLP-1 Weight Management",
        "service_target": "B2B GLP-1 Prescribing Suite (Doctors)",
        "title": "پروتکل علمی تعویض دارو (Switching) از اوزمپیک به مونجارو ویژه همکاران پزشک",
        "lines": [
            "هنگام تعویض داروی سماگلوتاید به تیرزپاتاید رعایت ۲ اصل بالینی حیاتی است:",
            "۱. شروع الزامی از پله اول دوز آغازین (تیرزپاتاید ۲.۵ میلی‌گرم) جهت جلوگیری از سمیت شدید گوارشی.",
            "۲. شروع داروی جدید دقیقا ۷ روز پس از آخرین تزریق داروی هفتگی قبلی.",
            "سوئیت بالینی آیویدیا نسخه ۱.۲ تمام محاسبات تیتراسیون و تعویض دارو را به صورت آنی برای پزشکان انجام می‌دهد."
        ],
        "cta": "مشاهده راهنمای تعویض دارو و سوئیت بالینی پزشکان",
        "url": URL_GLP1_DOCTOR_SUITE,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "15:30",
        "pillar": "Melasma & Sun Protection",
        "service_target": "Model 724 Skin AI",
        "title": "چرا لک‌های ملاسما در فصل تابستان پررنگ‌تر می‌شوند؟",
        "lines": [
            "سلول‌های رنگدانه‌ساز پوست (ملانوسیت‌ها) به حرارت، اشعه UVA و نور مرئی فوق‌العاده حساس‌اند.",
            "حتی نشستن کنار پنجره آفتاب‌گیر بدون ضدآفتاب می‌تواند زحمات چند ماهه درمان لک را از بین ببرد."
        ],
        "cta": "آنالیز آنلاین عمق و گستردگی لک‌های پوست",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "17:00",
        "pillar": "Skin Cancer Prevention",
        "service_target": "Model 1066 Skin Cancer Screening",
        "title": "آیا آفتاب‌سوختگی‌های دوران کودکی ریسک ملانوم را بالا می‌برند؟",
        "lines": [
            "مطالعات بالینی نشان می‌دهد سابقه بیش از ۵ بار آفتاب‌سوختگی شدید همراه با تاول در کودکی، ریسک ملانوم در بزرگسالی را دو برابر می‌کند.",
            "معاینات سالانه خال‌ها را جدی بگیرید."
        ],
        "cta": "اسکن و غربالگری هوشمند خال‌های بدن",
        "url": URL_SKIN_CANCER,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "18:30",
        "pillar": "Interactive Quiz",
        "service_target": "Model 724 Skin AI",
        "title": "کوئیز: آیا خشکی لب‌های شما ناشی از کمبود ویتامین است یا اگزمای لب؟",
        "lines": [
            "ترک‌خوردگی گوشه‌های لب (Angular Cheilitis) اغلب ناشی از کمبود ویتامین B2/B12 یا عفونت کاندیدا است.",
            "پوسته‌ریزی مداوم بدنه لب بیشتر به علت اگزمای تماسی با خمیردندان یا بالم‌های عطری رخ می‌دهد."
        ],
        "cta": "بررسی هوشمند علائم پوستی با آیویدیا",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "20:00",
        "pillar": "Online GP Spotlight",
        "service_target": "Online GP Doctor Visit",
        "title": "ویزیت آنلاین برای ارزیابی آزمایش‌های هورمونی، ریزش مو و آکنه هورمونی",
        "lines": [
            "اگر در سنین بزرگسالی دچار آکنه در ناحیه چانه و فک شده‌اید، بررسی هورمون‌های آندروژن و تخمدان پلی‌کیستیک (PCOS) توسط پزشک عمومی ضروری است."
        ],
        "cta": "درخواست ویزیت آنلاین و صدور نسخه آزمایش",
        "url": URL_ONLINE_GP,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "21:30",
        "pillar": "Evening Skincare Recap",
        "service_target": "Skin Routine Analyzer",
        "title": "چگونه رتینول را در روتین شبانه شروع کنیم بدون اینکه پوست پوسته پوسته شود؟",
        "lines": [
            "روش ساندویچی رتینول: ۱ لایه نازک مرطوب‌کننده ⬅️ رتینول به اندازه یک نخود ⬅️ مجدداً ۱ لایه مرطوب‌کننده سرامیدی.",
            "این روش تحریک پوستی را بدون کاهش اثربخشی ضد پیری به حداقل می‌رساند."
        ],
        "cta": "دریافت برنامه روتین مراقبت از پوست شخصی‌سازی‌شده",
        "url": URL_ROUTINE_ANALYZER,
        "has_photo": False,
        "photo_url": ""
    },

    # ==================== DAY 4 (Posts 31-40) ====================
    {
        "slot_time": "08:00",
        "pillar": "Morning Health Tip",
        "service_target": "Model 724 Skin AI",
        "title": "تفاوت کهیر حاد با بثورات دارویی (Drug Eruption)",
        "lines": [
            "کهیرهای گذرا معمولاً ظرف چند ساعت محو می‌شوند، اما بثورات ناشی از حساسیت دارویی ثابت مانده و ممکن است با تب همراه باشند.",
            "قطع داروی مسبب تحت نظر پزشک فوری‌ترین اقدام است."
        ],
        "cta": "آنالیز آنلاین بثورات پوستی با هوش مصنوعی",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "09:30",
        "pillar": "AI Case Study",
        "service_target": "Model 724 Skin AI",
        "title": "کیس واقعی: تشخیص پیتریازیس روزه‌آ (Pityriasis Rosea) و پلاک پیش‌قراول",
        "lines": [
            "بیمار با یک لکه بیضی بزرگ روی قفسه سینه و سپس دانه‌های کوچک شبیه درخت کاج در پشت مراجعه کرد.",
            "مدل ۷۲۴ بیماری خود‌محدود‌شونده پیتریازیس روزه‌آ را با اطمینان تشخیص داد."
        ],
        "cta": "اسکن و تحلیل ضایعات پوستی با مدل ۷۲۴",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "11:00",
        "pillar": "Skin Routine Guide",
        "service_target": "Skin Routine Analyzer",
        "title": "راز استفاده از ویتامین C و نیاسینامید در یک روتین پوستی",
        "lines": [
            "افسانه تداخل ویتامین C با نیاسینامید منسوخ شده است. فرمولاسیون‌های مدرن این دو ترکیب را برای روشن‌سازی پوست فوق‌العاده موثر کرده‌اند."
        ],
        "cta": "دریافت اختصاصی روتین پوستی ضد لک و روشن‌کننده",
        "url": URL_ROUTINE_ANALYZER,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "12:30",
        "pillar": "Interactive Quiz",
        "service_target": "Model 724 Skin AI",
        "title": "تست: آیا پوسته سر شما شوره خشک است یا شوره چرب؟",
        "lines": [
            "شوره‌های ریز و سفید که روی شانه‌ها می‌ریزند شوره خشک هستند، در حالی که پوسته‌های ضخیم و زرد چسبنده نشانه تکثیر قارچ مالاسزیا در شوره چرب است."
        ],
        "cta": "آنالیز آنلاین مشکلات کف سر و مو با آیویدیا",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "14:00",
        "pillar": "GLP-1 Weight Management",
        "service_target": "B2C GLP-1 Need Assessment & Referral",
        "title": "شاخص توده بدنی (BMI) و شرایط بالینی دریافت نسخه داروهای لاغری",
        "lines": [
            "طبق گایدلاین‌های جهانی، چه کسانی مجاز به دریافت داروهای GLP-1 هستند؟",
            "🔹 شاخص BMI بالاتر از ۳۰ (چاقی بالینی).",
            "🔹 شاخص BMI بالاتر از ۲۷ همراه با حداقل یک بیماری متابولیک (دیابت نوع ۲، کبد چرب گرید ۲، سندرم متابولیک).",
            "ابزار غربالگری آیویدیا شرایط شما را به صورت کاملاً علمی ارزیابی کرده و امکان ویزیت فوری توسط پزشک را فراهم می‌کند."
        ],
        "cta": "محاسبه آنلاین BMI و ارزیابی شرایط بالینی دریافت نسخه",
        "url": URL_GLP1_B2C_ASSESSMENT,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "15:30",
        "pillar": "Melasma & Sun Protection",
        "service_target": "Model 724 Skin AI",
        "title": "آیا نور صفحه نمایش گوشی و مانیتور (Blue Light) باعث لک صورت می‌شود؟",
        "lines": [
            "نور آبی HEV می‌تواند ملانوسیت‌ها را تحریک کرده و لک‌های ملاسما را تیره کند. استفاده از ضدآفتاب‌های حاوی اکسید آهن محافظت کامل در برابر نور آبی ایجاد می‌کند."
        ],
        "cta": "آنالیز پوست و راهنمای ضدآفتاب مناسب شما",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "17:00",
        "pillar": "Skin Cancer Prevention",
        "service_target": "Model 1066 Skin Cancer Screening",
        "title": "کراتوز اکتینیک (Actinic Keratosis)؛ ضایعات خشن پیش‌سرطانی پوست",
        "lines": [
            "ضایعات زبر و پوسته‌دار شبیه سمباده روی صورت یا پشت دست ناشی از تابش مزمن آفتاب است و می‌تواند به کارسینوم سلول سنگفرشی (SCC) تبدیل شود."
        ],
        "cta": "اسکن آنلاین ضایعات زبر و مشکوک پوستی با هوش مصنوعی",
        "url": URL_SKIN_CANCER,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "18:30",
        "pillar": "Interactive Quiz",
        "service_target": "Model 724 Skin AI",
        "title": "کوئیز: فرق خشکی پوست با بیماری ایکتیوز (پوست ماهی)",
        "lines": [
            "ایکتیوز یک اختلال ژنتیکی شاخی شدن پوست است که پوسته‌های چندضلعی شبیه فلس ماهی ایجاد می‌کند و نیازمند شوینده‌های حاوی اوره ۱۰٪ به بالا است."
        ],
        "cta": "آنالیز تخصصی نوع خشکی پوست با آیویدیا",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "20:00",
        "pillar": "Online GP Spotlight",
        "service_target": "Online GP Doctor Visit",
        "title": "مشاوره آنلاین برای نسخه داروهای فشار خون، دیابت و چربی",
        "lines": [
            "تمدید نسخه‌های روتین پزشکی بدون نیاز به رفت‌و‌آمد و ایستادن در صف مطب‌ها با پزشک عمومی آیویدیا."
        ],
        "cta": "شروع ویزیت آنلاین پزشک عمومی",
        "url": URL_ONLINE_GP,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "21:30",
        "pillar": "Evening Skincare Recap",
        "service_target": "Skin Routine Analyzer",
        "title": "روتین مراقبت از دست‌ها در برابر پیری زودرس و لک‌های قهوه‌ای",
        "lines": [
            "پوست دست نازک‌تر از صورت است و زودتر پیر می‌شود. شب‌ها از کرم‌های حاوی نیاسینامید و سرامید و در روز از ضدآفتاب روی پشت دست استفاده کنید."
        ],
        "cta": "دریافت برنامه کامل روتین مراقبت از پوست",
        "url": URL_ROUTINE_ANALYZER,
        "has_photo": False,
        "photo_url": ""
    },

    # ==================== DAY 5 (Posts 41-50) ====================
    {
        "slot_time": "08:00",
        "pillar": "Morning Health Tip",
        "service_target": "Model 724 Skin AI",
        "title": "اگزمای دست در اثر مواد شوینده خانگی؛ چگونه از دست‌ها محافظت کنیم؟",
        "lines": [
            "ترکیبات قلیایی سفیدکننده‌ها چربی محافظ پوست را حل می‌کنند. همیشه زیر دستکش لاستیکی از دستکش نخی استفاده کنید و بلافاصله کرم ترمیم‌کننده بزنید."
        ],
        "cta": "تشخیص شدت آسیب سد دفاعی پوست با هوش مصنوعی",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "09:30",
        "pillar": "AI Case Study",
        "service_target": "Model 724 Skin AI",
        "title": "کیس واقعی: تشخیص بیماری زونا (Herpes Zoster) در مسیر عصب بین‌دنده‌ای",
        "lines": [
            "بیمار با سوزش شدید یک‌طرفه و دانه‌های قرمز خوشه‌ای مراجعه کرد. مدل ۷۲۴ زونا را تشخیص داده و ضرورت شروع داروی ضد ویروس والاسیکلوویر ظرف ۷۲ ساعت اول را یادآور شد."
        ],
        "cta": "تشخیص آنلاین و سریع ضایعات پوستی با مدل ۷۲۴",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "11:00",
        "pillar": "Skin Routine Guide",
        "service_target": "Skin Routine Analyzer",
        "title": "آزالائیک اسید؛ ترکیب جادویی برای آکنه، قرمزی روزاسه و لک",
        "lines": [
            "آزالائیک اسید ۱۰٪ یا ۲۰٪ یک ترکیب چندکاره بی‌نظیر و ایمن در بارداری است که التهاب را کاهش داده و باکتری آکنه را مهار می‌کند."
        ],
        "cta": "دریافت برنامه روتین اختصاصی پوست حساس",
        "url": URL_ROUTINE_ANALYZER,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "12:30",
        "pillar": "Interactive Quiz",
        "service_target": "Model 724 Skin AI",
        "title": "تست: آیا جوش‌های ریز پیشانی شما آکنه قارچی (مالاسزیا فولیکولیت) است؟",
        "lines": [
            "اگر جوش‌های ریز هم‌اندازه و خارش‌دار روی پیشانی دارید که به داروهای آکنه عادی پاسخ نمی‌دهند، احتمال آکنه قارچی بسیار بالاست."
        ],
        "cta": "آنالیز آنلاین جوش‌های مقاوم با هوش مصنوعی آیویدیا",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "14:00",
        "pillar": "GLP-1 Weight Management",
        "service_target": "B2B GLP-1 Doctor Network (Doctors)",
        "title": "عضویت پزشکان در شبکه ارجاع بالینی آیویدیا و دسترسی به سوئیت محاسباتی GLP-1",
        "lines": [
            "پزشکان عمومی، متخصصین غدد و داخلی می‌توانند با ثبت‌نام رایگان در شبکه همکاران آیویدیا:",
            "🔹 بیماران ارزیابی‌شده در سامانه B2C را با نامه ارجاع رسمی در مطب خود پذیرش کنند.",
            "🔹 از ابزار دوزبندی پیشرفته و پرینت استاندارد نسخه‌های A4 استفاده نمایند.",
            "🔹 به زنجیره دارویی معتبر و سهمیه اصیل جهت درمان مراجعین دسترسی داشته باشند."
        ],
        "cta": "عضویت رایگان در شبکه ارجاع پزشکان آیویدیا",
        "url": URL_GLP1_DOCTOR_SUITE,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "15:30",
        "pillar": "Melasma & Sun Protection",
        "service_target": "Model 724 Skin AI",
        "title": "سرم ترانگزامیک اسید (Tranexamic Acid) چگونه لک‌های مقاوم را محو می‌کند؟",
        "lines": [
            "این ترکیب ارتباط بین سلول‌های کراتینوسیت و ملانوسیت را قطع کرده و از فعال شدن تولید رنگدانه در اثر تابش UV جلوگیری می‌کند."
        ],
        "cta": "تحلیل هوشمند لک‌های پوستی و درمان اختصاصی",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "17:00",
        "pillar": "Skin Cancer Prevention",
        "service_target": "Model 1066 Skin Cancer Screening",
        "title": "تفاوت خال دیسپلاستیک (خال آتیپیک) با ملانوم خطرناک",
        "lines": [
            "خال‌های دیسپلاستیک خوش‌خیم ولی نامنظم هستند. غربالگری دوره‌ای برای رصد هرگونه تغییر در مرز و رنگ این خال‌ها حیاتی است."
        ],
        "cta": "غربالگری هوشمند خال‌های مشکوک با مدل ۱۰۶۶",
        "url": URL_SKIN_CANCER,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "18:30",
        "pillar": "Interactive Quiz",
        "service_target": "Model 724 Skin AI",
        "title": "کوئیز: آیا ریزش موی شما ناشی از کمبود آهن است یا استرس شدید (تلوژن افلوویوم)؟",
        "lines": [
            "ریزش مویی که ۲ تا ۳ ماه بعد از یک استرس شدید، جراحی یا رژیم سخت رخ می‌دهد تلوژن افلوویوم نام دارد و موقتی است."
        ],
        "cta": "بررسی هوشمند الگوی ریزش مو با آیویدیا",
        "url": URL_SKIN_AI,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "20:00",
        "pillar": "Online GP Spotlight",
        "service_target": "Online GP Doctor Visit",
        "title": "نسخه آنلاین داروهای تخصصی پوست و درمان‌های ضد قارچ و آنتی‌بیوتیک",
        "lines": [
            "دریافت مشاوره پزشکی، بررسی بالینی تصاویر ضایعات و صدور نسخه معتبر توسط پزشک عمومی در کمتر از چند دقیقه."
        ],
        "cta": "درخواست ویزیت آنلاین پزشک عمومی",
        "url": URL_ONLINE_GP,
        "has_photo": False,
        "photo_url": ""
    },
    {
        "slot_time": "21:30",
        "pillar": "Evening Skincare Recap",
        "service_target": "Skin Routine Analyzer",
        "title": "راهنمای مراقبت از پوست در خواب؛ چگونه شب‌ها پوست بازسازی می‌شود؟",
        "lines": [
            "جریان خون پوست در شب افزایش می‌یابد و جذب اکتیوهای ترمیمی به حداکثر می‌رسد. روتین شبانه را حداقل ۳۰ دقیقه قبل از خواب انجام دهید."
        ],
        "cta": "دریافت برنامه روتین اختصاصی پوست شما",
        "url": URL_ROUTINE_ANALYZER,
        "has_photo": False,
        "photo_url": ""
    }
]

def replenish():
    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found: {DB_PATH}")
        return 0

    with open(DB_PATH, "r", encoding="utf-8") as f:
        posts = json.load(f)

    pending_count = sum(1 for p in posts if p.get("status") == "pending")
    published_count = sum(1 for p in posts if p.get("status") == "published")
    max_id = max((p.get("id", 0) for p in posts), default=0)

    print(f"📊 Current Posts Status — Total: {len(posts)} | Published: {published_count} | Pending: {pending_count}")

    if pending_count < 20:
        print(f"⚡ Pending post queue is below threshold ({pending_count} < 20). Generating fresh posts batch...")
        
        added_count = 0
        for item in POSTS_CATALOG:
            max_id += 1
            added_count += 1
            utm = f"post_{max_id}_{item['slot_time'].replace(':', '')}"
            
            p_title = item["title"]
            p_lines = item["lines"]
            p_cta = item["cta"]
            p_url = item["url"]
            
            text = f"📌 <b>{p_title}</b>\n\n" + "\n\n".join(p_lines) + "\n\n"
            text += f"👉 <a href='{p_url}?utm_source=telegram&utm_medium=channel&utm_campaign={utm}'>{p_cta}</a>\n\n"
            text += f"{FORWARD_PROMPT}\n\n{CHANNEL_SIGNATURE}"
            
            posts.append({
                "id": max_id,
                "slot_time": item["slot_time"],
                "pillar": item["pillar"],
                "service_target": item["service_target"],
                "title": p_title,
                "text": text,
                "has_photo": item.get("has_photo", False),
                "photo_url": item.get("photo_url", ""),
                "utm_campaign": utm,
                "status": "pending",
                "published_at": None,
                "telegram_message_id": None
            })

        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)

        print(f"✅ Added {added_count} new posts. Total posts in database: {len(posts)} (Pending: {pending_count + added_count})")
        return added_count
    else:
        print(f"ℹ️ Queue healthy ({pending_count} pending). No immediate replenishment needed.")
        return 0

if __name__ == "__main__":
    replenish()
