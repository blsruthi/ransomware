import hashlib
import os
import smtplib
from email.mime.text import MIMEText
# File to monitor
TARGET_FILE = "admin.html"
HASH_FILE = "admin_hash.txt"

def hash_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

# First time run: save the legitimate hash
def save_original_hash():
    h = hash_file(TARGET_FILE)
    with open(HASH_FILE, "w") as f:
        f.write(h)
    print("✅ Baseline hash saved.")

# Run this to check if file changed
def detect_change():
    if not os.path.exists(HASH_FILE):
        print("❗ Baseline hash not found. Run save_original_hash() first.")
        return

    original_hash = open(HASH_FILE).read().strip()
    current_hash = hash_file(TARGET_FILE)

    if original_hash != current_hash:
        print("🚨 ALERT: admin.html has been modified (possible ransomware).")
       
        send_email_alert()
    else:
        print("✅ admin.html is clean and unchanged.")
import smtplib
from email.mime.text import MIMEText

def send_email_alert():
    sender = "blsruthi12@gmail.com"
    receiver = "boyalakshmisruthi@gmail.com"
    app_password = "cpxzvjpucaziwtuf"  # generated from Gmail

    msg = MIMEText("🚨 ALERT: Ransomware modification detected in admin page.")
    msg["Subject"] = "🔥 Ransomware Alert Detected"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender, app_password)
        server.send_message(msg)
        server.quit()
        print("📧 Email alert sent to admin.")
    except Exception as e:
        print("❌ Failed to send email:", e)


# === Choose what to run ===
#save_original_hash()     # Run this only ONCE when admin.html is clean
detect_change()            # Run this to detect tampering
