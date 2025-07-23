from urllib.parse import urljoin

SITES = {
    "eurointegration_articles": {
        "name": "Європейська правда. Статті",
        "url": "https://www.eurointegration.com.ua/articles/",
        "base_url": "https://www.eurointegration.com.ua",
        # CSS selector for each article block on the listing page:
        "item_selector": ".block_stories .article",        # ← adjust if needed
        # From each block, how to get title, link, date, description:
        "title_selector": ".article__title a",
        "link_selector": ".article__title a",
        "date_selector": ".article__date",          # ← adjust if needed
        "description_selector": ".article__subtitle",    # optional
        # Helper to absolutize links:
        "make_link": lambda href: urljoin("https://www.eurointegration.com.ua/", href),
    },
    "forbes_articles": {
        "name": "Forbes",
        "url": "https://forbes.ua/top-articles-forbes-ukraine/",
        "base_url": "https://forbes.ua/",
        # CSS selector for each article block on the listing page:
        "item_selector": ".c-feed-inner .c-entry-content",        # ← adjust if needed
        # From each block, how to get title, link, date, description:
        "title_selector": "a.c-entry-link",
        "link_selector": "a.c-entry-link",
        "date_selector": "time",          # ← adjust if needed
        "description_selector": "a.c-entry-link",    # optional
        # Helper to absolutize links:
        "make_link": lambda href: urljoin("https://www.forbes.ua/", href),
    },
    "economist": {
        "name": "Economist",
        "url": "https://www.economist.com/weeklyedition/2025-07-19/",
        "base_url": "https://www.economist.com/",
        # CSS selector for each article block on the listing page:
        "item_selector": "",        # ← adjust if needed
        # From each block, how to get title, link, date, description:
        "title_selector": "h3 a",
        "link_selector": "h3 a",
        "date_selector": "time",          # ← adjust if needed
        "description_selector": "p",    # optional
        # Helper to absolutize links:
        "make_link": lambda href: urljoin("https://www.economist.com/", href),
    },
    "babel_news": {
        "name": "Бабель",
        "url": "https://t.me/s/babel",
        "base_url": "https://t.me/s/babel",
        # CSS selector for each article block on the listing page:
        "item_selector": ".tgme_channel_history .tgme_widget_message_wrap",        # ← adjust if needed
        # From each block, how to get title, link, date, description:
        "title_selector": ".tgme_widget_message_text.js-message_text",
        "link_selector": ".tgme_widget_message_date",
        "date_selector": ".time",          # ← adjust if needed
        "description_selector": ".tgme_widget_message_text.js-message_text",    # optional
        # Helper to absolutize links:
        "make_link": lambda href: urljoin("https://t.me/s/babel/", href),
    },
    "milinua": {
        "name": "Мілітарний",
        "url": "https://t.me/s/milinua",
        "base_url": "https://t.me/s/milinua",
        # CSS selector for each article block on the listing page:
        "item_selector": ".tgme_channel_history .tgme_widget_message_wrap",        # ← adjust if needed
        # From each block, how to get title, link, date, description:
        "title_selector": ".tgme_widget_message_text.js-message_text",
        "link_selector": ".tgme_widget_message_date",
        "date_selector": ".time",          # ← adjust if needed
        "description_selector": ".tgme_widget_message_text.js-message_text",    # optional
        # Helper to absolutize links:
        "make_link": lambda href: urljoin("https://t.me/s/milinua/", href),
    },
    "yigal_levin": {
        "name": "YIGAL LEVIN",
        "url": "https://t.me/s/yigal_levin",
        "base_url": "https://t.me/s/yigal_levin",
        # CSS selector for each article block on the listing page:
        "item_selector": ".tgme_channel_history .tgme_widget_message_wrap",        # ← adjust if needed
        # From each block, how to get title, link, date, description:
        "title_selector": ".tgme_widget_message_text.js-message_text",
        "link_selector": ".tgme_widget_message_date",
        "date_selector": ".time",          # ← adjust if needed
        "description_selector": ".tgme_widget_message_text.js-message_text",    # optional
        # Helper to absolutize links:
        "make_link": lambda href: urljoin("https://t.me/s/yigal_levin/", href),
    },
    "railinsider": {
        "name": "Rail Insider",
        "url": "https://t.me/s/railinsider",
        "base_url": "https://t.me/s/railinsider",
        # CSS selector for each article block on the listing page:
        "item_selector": ".tgme_channel_history .tgme_widget_message_wrap",        # ← adjust if needed
        # From each block, how to get title, link, date, description:
        "title_selector": ".tgme_widget_message_text.js-message_text",
        "link_selector": ".tgme_widget_message_date",
        "date_selector": ".time",          # ← adjust if needed
        "description_selector": ".tgme_widget_message_text.js-message_text",    # optional
        # Helper to absolutize links:
        "make_link": lambda href: urljoin("https://t.me/s/railinsider/", href),
    },
    "ames": {
        "name": "AMES",
        "url": "https://t.me/s/middle_east_review",
        "base_url": "https://t.me/s/middle_east_review",
        # CSS selector for each article block on the listing page:
        "item_selector": ".tgme_channel_history .tgme_widget_message_wrap",        # ← adjust if needed
        # From each block, how to get title, link, date, description:
        "title_selector": ".tgme_widget_message_text.js-message_text",
        "link_selector": ".tgme_widget_message_date",
        "date_selector": ".time",          # ← adjust if needed
        "description_selector": ".tgme_widget_message_text.js-message_text",    # optional
        # Helper to absolutize links:
        "make_link": lambda href: urljoin("https://t.me/s/middle_east_review/", href),
    },
    "ein_fruhling_2": {
        "name": "Богдан Кротевич",
        "url": "https://t.me/s/ein_fruhling_2",
        "base_url": "https://t.me/s/ein_fruhling_2",
        # CSS selector for each article block on the listing page:
        "item_selector": ".tgme_channel_history .tgme_widget_message_wrap",        # ← adjust if needed
        # From each block, how to get title, link, date, description:
        "title_selector": ".tgme_widget_message_text.js-message_text",
        "link_selector": ".tgme_widget_message_date",
        "date_selector": ".time",          # ← adjust if needed
        "description_selector": ".tgme_widget_message_text.js-message_text",    # optional
        # Helper to absolutize links:
        "make_link": lambda href: urljoin("https://t.me/s/ein_fruhling_2/", href),
    },
    "silukr": {
        "name": "Сіль",
        "url": "https://t.me/s/silukr",
        "base_url": "https://t.me/s/silukr",
        # CSS selector for each article block on the listing page:
        "item_selector": ".tgme_channel_history .tgme_widget_message_wrap",        # ← adjust if needed
        # From each block, how to get title, link, date, description:
        "title_selector": ".tgme_widget_message_text.js-message_text",
        "link_selector": ".tgme_widget_message_date",
        "date_selector": ".time",          # ← adjust if needed
        "description_selector": ".tgme_widget_message_text.js-message_text",    # optional
        # Helper to absolutize links:
        "make_link": lambda href: urljoin("https://t.me/s/silukr/", href),
    },
    "thinktankces": {
        "name": "Що з економікою?",
        "url": "https://t.me/s/thinktankces",
        "base_url": "https://t.me/s/thinktankces",
        # CSS selector for each article block on the listing page:
        "item_selector": ".tgme_channel_history .tgme_widget_message_wrap",        # ← adjust if needed
        # From each block, how to get title, link, date, description:
        "title_selector": ".tgme_widget_message_text.js-message_text",
        "link_selector": ".tgme_widget_message_date",
        "date_selector": ".time",          # ← adjust if needed
        "description_selector": ".tgme_widget_message_text.js-message_text",    # optional
        # Helper to absolutize links:
        "make_link": lambda href: urljoin("https://t.me/s/thinktankces/", href),
    },
    "metaTCG": {
        "name": "ТГК и метафан",
        "url": "https://t.me/s/metaTCG",
        "base_url": "https://t.me/s/metaTCG",
        # CSS selector for each article block on the listing page:
        "item_selector": ".tgme_channel_history .tgme_widget_message_wrap",        # ← adjust if needed
        # From each block, how to get title, link, date, description:
        "title_selector": ".tgme_widget_message_text.js-message_text",
        "link_selector": ".tgme_widget_message_date",
        "date_selector": ".time",          # ← adjust if needed
        "description_selector": ".tgme_widget_message_text.js-message_text",    # optional
        # Helper to absolutize links:
        "make_link": lambda href: urljoin("https://t.me/s/metaTCG/", href),
    },
    "maxua_public": {
        "name": "maxua posts",
        "url": "https://t.me/s/maxua_public",
        "base_url": "https://t.me/s/maxua_public",
        # CSS selector for each article block on the listing page:
        "item_selector": ".tgme_channel_history .tgme_widget_message_wrap",        # ← adjust if needed
        # From each block, how to get title, link, date, description:
        "title_selector": ".tgme_widget_message_text.js-message_text",
        "link_selector": ".tgme_widget_message_date",
        "date_selector": ".time",          # ← adjust if needed
        "description_selector": ".tgme_widget_message_text.js-message_text",    # optional
        # Helper to absolutize links:
        "make_link": lambda href: urljoin("https://t.me/s/maxua_public/", href),
    },
    # You can add more sites here...
}
