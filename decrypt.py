from cryptography.fernet import Fernet
import os

TARGET_FILE = "admin.html"
KEY_FILE = "key.key"
ENCRYPTED_BACKUP = "admin_backup.encrypted"

def load_key():
    return open(KEY_FILE, "rb").read()

def decrypt_file():
    key = load_key()
    fernet = Fernet(key)

    with open(ENCRYPTED_BACKUP, "rb") as backup_file:
        encrypted_data = backup_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(TARGET_FILE, "wb") as target_file:
        target_file.write(decrypted_data)

    print(f"✅ Restored {TARGET_FILE} successfully.")

decrypt_file()
