from cryptography.fernet import Fernet
import os

# === CONFIG ===
TARGET_FILE = "admin.html"
BLOCKED_FILE = "blocked.html"
KEY_FILE = "key.key"
ENCRYPTED_BACKUP = "admin_backup.encrypted"

# Step 1: Generate a key if missing
def write_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        print("🔑 Key generated.")
    else:
        print("✅ Key already exists.")

# Step 2: Load the key
def load_key():
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError("❌ key.key not found! Run write_key() first.")
    return open(KEY_FILE, "rb").read()

# Step 3: Encrypt original HTML and replace with blocked content
def encrypt_and_block():
    key = load_key()
    fernet = Fernet(key)

    # Encrypt original content
    with open(TARGET_FILE, "rb") as original_file:
        original_data = original_file.read()

    encrypted_data = fernet.encrypt(original_data)

    # Save encrypted backup
    with open(ENCRYPTED_BACKUP, "wb") as backup_file:
        backup_file.write(encrypted_data)
    print(f"🔐 Encrypted backup saved as: {ENCRYPTED_BACKUP}")

    # Replace with blocked.html content
    with open(BLOCKED_FILE, "rb") as blocked_file:
        blocked_data = blocked_file.read()

    with open(TARGET_FILE, "wb") as target_file:
        target_file.write(blocked_data)
    print(f"🚫 {TARGET_FILE} is now blocked.")

# Run everything
write_key()
encrypt_and_block()
