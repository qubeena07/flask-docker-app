import os, time, requests

TARGET = os.getenv("TARGET", "http://web:8000/health")
WEBHOOK = os.environ.get("https://discord.com/api/webhooks/your_webhook_url")  # Replace with your Discord webhook URL
INTERVAL = int(os.getenv("CHECK_INTERVAL", "5"))

def send_discord(msg):
    if not WEBHOOK:
        print("No webhook URL provided. Msg:", msg)
        return
    try:
        r = requests.post(WEBHOOK, json={"content": msg}, timeout=10)
        r.raise_for_status()
        print("✅ Discord notification sent:", msg)
    except Exception as e:
        print("❌ Failed to send Discord notification:", e)

while True:
    try:
        r = requests.get(TARGET, timeout=10)
        if r.status_code != 200:
            send_discord(f"[Monitor] {TARGET} returned {r.status_code}")
            print(f"❌ Bad status {r.status_code}")
        else:
            print(f"✅ {TARGET} is healthy ({r.status_code})")
    except Exception as e:
        # This now catches DNS errors, connection errors, timeouts, etc.
        send_discord(f"[Monitor] Could not reach {TARGET}: {e}")
        print(f"❌ Exception: {e}")
    time.sleep(INTERVAL)