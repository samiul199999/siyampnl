import threading
import time
import requests
from datetime import datetime

# --- Logic Configuration ---
def run_bot(name, url, delay):
    while True:
        start = time.time()
        try:
            # JS had 10s timeout
            res = requests.get(url, timeout=10)
            
            took = time.time() - start
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [{name}] {url} -> {res.status_code} ({took:.2f}s)")
            
        except Exception as e:
            took = time.time() - start
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [{name}] Error: {e} ({took:.2f}s)")

        # Python sleep takes seconds
        time.sleep(delay)

# --- URL Groups ---
urls_3sec = [
    "https://siyamonline.xyz/4sec1.php",
    "https://siyamonline.xyz/4sec2.php",
    "https://siyamonline.xyz/4sec3.php",
    "https://siyamonline.xyz/4sec4.php",
    "https://siyamonline.xyz/4sec5.php",
    "https://siyamonline.xyz/4sec6.php",
    "https://siyamonline.xyz/4sec7.php",
    "https://siyamonline.xyz/4sec8.php",
    "https://siyamonline.xyz/4sec9.php",
    "https://siyamonline.xyz/4sec12.php",
    "https://siyamonline.xyz/4sec13.php",
    "https://earnifyteam.xyz/4sec2.php",
    "https://siyamonline.xyz/4sec11.php",
]

special_bots = [
    {"name": "jimkar bot", "url": "https://siyamonline.xyz/4sec10.php", "delay": 3},
    {"name": "talhannc bot", "url": "https://earnifyteam.xyz/4sec1.php", "delay": 2},
]

# --- Execution ---
if __name__ == "__main__":
    # Start 3-sec bots
    for i, url in enumerate(urls_3sec):
        name = f"bot{i + 1}"
        t = threading.Thread(target=run_bot, args=(name, url, 3))
        t.daemon = True
        t.start()

    # Start special bots
    for bot in special_bots:
        t = threading.Thread(target=run_bot, args=(bot["name"], bot["url"], bot["delay"]))
        t.daemon = True
        t.start()

    # Keep process alive
    while True:
        time.sleep(60)
