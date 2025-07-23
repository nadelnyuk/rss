import os,re
import logging
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import dateparser
from datetime import datetime, timezone
from feedgen.feed import FeedGenerator
from config import SITES

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")

FEEDS_DIR = os.path.join(os.path.dirname(__file__), "feeds")
os.makedirs(FEEDS_DIR, exist_ok=True)

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

def fetch_items(site_conf):
    """Fetch and parse items from one site listing page."""
    resp = requests.get(site_conf["url"], timeout=10, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    items = []
    if 'economist' in site_conf["url"]:
        articles = soup.find_all("div", attrs={"data-test-id": "teaser"})
    else:
        articles = soup.select(site_conf["item_selector"])

    for block in articles:
        # Title & link
        a = block.select_one(site_conf["link_selector"])
        
        href = a["href"]
        link = site_conf["make_link"](href)

        # Publication date
        if 't.me' in site_conf["url"]:
            #title = a.get_text(strip=True)
            date_text = block.select_one(site_conf["date_selector"]).get('datetime') if block.select_one(site_conf["date_selector"]) else ''

            desc_block = block.select(site_conf.get("description_selector", ""))[0]
            description = f"""
                <![CDATA[
                {desc_block}
                ]]>
            """
            
            first_chunk = re.split(r'(?i)<br\s*/?>', str(desc_block), maxsplit=1)[0]
            title = BeautifulSoup(first_chunk, 'html.parser').get_text(strip=False)
        elif 'forbes' in site_conf["url"]:
            title = a.get_text(strip=True)
            date_text = block.select_one(site_conf["date_selector"]).get('datetime') if block.select_one(site_conf["date_selector"]) else ''
            description = ''
        elif 'economist' in site_conf["url"]:
            title = a.get_text(strip=True)
            date_text = ''
            desc_block = block.select(site_conf.get("description_selector", ""))[-1]
            description = f"""
                <![CDATA[
                {desc_block}
                ]]>
            """
        else:
            title = a.get_text(strip=True)
            date_text = block.select_one(site_conf["date_selector"]).get_text(strip=True).split(',')[0] if block.select_one(site_conf["date_selector"]) else ''

            desc_block = block.select_one(site_conf.get("description_selector", ""))
            description = desc_block.get_text(strip=True) if desc_block else ""
        dt = dateparser.parse(date_text, languages=["uk","ru","en"])
        if not dt:
            # fallback to “now” as UTC
            dt = datetime.now(timezone.utc)
        # if it’s naïve, assume UTC (or change to your local zone)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)

        # now format with %z and you’ll get “+0000”
        pubDate = dt.strftime("%a, %d %b %Y %H:%M:%S %z")
        

        items.append({
            "title": title,
            "link": link,
            "pubDate": pubDate,
            "description": description,
        })

    return items

def build_feed(site_key, items):
    """Use feedgen to produce a valid RSS 2.0 file."""
    conf = SITES[site_key]
    fg = FeedGenerator()
    fg.title(conf["name"])
    fg.link(href=conf["url"], rel="alternate")
    fg.description(f"Latest: {conf['name']}")
    fg.language("uk")

    for itm in items:
        fe = fg.add_entry()
        fe.id(itm["link"])
        fe.title(itm["title"])
        fe.link(href=itm["link"])
        fe.pubDate(itm["pubDate"])
        if itm["description"]:
            fe.description(itm["description"])

    out_path = os.path.join(FEEDS_DIR, f"{site_key}.xml")
    fg.rss_file(out_path)
    
    return len(items), out_path

def main():
    for site_key in SITES:
        try:
            logging.info(f"Fetching {site_key}…")
            items = fetch_items(SITES[site_key])
            count, feed_path = build_feed(site_key, items)
            logging.info(f"  → {count} items written to {feed_path}")
        except Exception as e:
            logging.error(f"Error for {site_key}: {e}")

if __name__ == "__main__":
    main()
