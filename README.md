# 🛡️ Ransomware Simulation and Detection System

This project is a simulation and partial detection system for ransomware behavior, built with Python and a simple web-based interface. It includes file encryption/decryption, user login systems, role-based access (admin/user), and logging mechanisms.

---

## 🔍 Features

- 🔐 **Encrypt & Decrypt Files** using a generated key (`key.key`)
- 🔑 **Admin and User Login** interface (`admin_login.html`, `login.html`, `signup.html`)
- 🚫 **Blocked Access Page** when ransomware is detected
- 📜 **Role Selection Interface**
- 🛠 **Ransomware simulation script** (`ransome.py`, `encrypt.py`, `decrypt.py`)
- 🔎 **Basic detection logic** (`dector.py`, `detector.py`)
- 📁 **Encrypted backup handling** (`admin_backup.encrypted`)
- 🎨 **Styled with custom `style.css`**

---

## 📂 Project Structure

├── admin.html # Admin dashboard
├── admin_alogin.html # Admin login page
├── admin_backup.encrypted # Encrypted data backup
├── admin_hash.txt # Admin password hash (example)
├── blocked.html # Blocked access interface
├── data.txt # Test file for data input/output
├── decrypt.py # Decryption logic
├── dector.py / detector.py # Detection logic (possibly one is a typo)
├── encrypt.py # Encryption logic
├── home.html # Main homepage
├── key.key # Encryption key file
├── login.html # Login page for users
├── ransome.py # Ransomware simulation script
├── select_role.html # Role selection interface
├── signup.html # Signup page
├── style.css # CSS styling

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/blsruthi/ransomware.git
cd ransomware
## 🎥 Ransomware Simulation Demo

[📥 Click here to download and watch the demo](ransomeware.mp4)
