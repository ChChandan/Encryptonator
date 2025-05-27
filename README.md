
# 🔐 Encryptonator - File Encryption Tool

**Encryptonator** is a Python-based file encryption utility with a graphical user interface (GUI) designed to help users securely encrypt, decrypt, and manage sensitive files using a password-derived key. It also features restricted file protection and a secure delete option for enhanced privacy.

## 🧩 Features

* 🔐 **Password-Based Encryption** using `cryptography.fernet`
* 🧪 **Password Strength Validation**
* 🗝️ **Key Generation with PBKDF2HMAC**
* 🖼️ **User-Friendly GUI** built with `Tkinter` and `ttk`
* ⚠️ **System Path Protection** (prevents encrypting core OS directories)
* 🧹 **Secure File Deletion** with overwriting method
* 📁 **File Picker Interface** for both key and file selection

---

## 📸 GUI Screenshots

* **Key Generator**
  Allows users to create strong, validated keys from custom passwords.

* **Main Tool**
  Choose files to encrypt or decrypt using the generated key.

---

## 🛠 Installation

### Prerequisites

* Python 3.8 or above
* Required libraries:

  ```bash
  pip install cryptography
  ```

---

## 🚀 How to Use

1. **Generate a Key**

   * Launch the GUI.
   * Navigate to the "Generate Key" section.
   * Enter a strong password (at least 8 characters, with numbers and special characters).
   * A key file (`<username>.key`) will be saved in the working directory.

2. **Encrypt a File**

   * Select the file you want to encrypt (e.g., `confidential.txt`).
   * Provide the key file.
   * File contents will be securely encrypted.

3. **Decrypt a File**

   * Provide the encrypted file and key file.
   * Decrypted content will be restored in-place.

4. **Secure Delete (optional - terminal only)**

   * Securely overwrite and delete a file with randomized content.

---

## ⛔ Restricted Zones

To protect the system, encryption of files located in sensitive directories is blocked:

* **Windows:** `C:\Windows`, `C:\Users`, etc.
* **Linux/macOS:** `/usr`, `/etc`, `/bin`, `/System`, etc.

---

## 🔐 Password Rules

* Minimum 8 characters
* Must start with a letter
* Must include:

  * At least one digit
  * At least one special character (`@_!#$%^&*<>?~:`)

---

## 🧑‍💻 Developer Notes

* Encryption is done using `Fernet` symmetric key encryption (AES in CBC mode with HMAC).
* Key derivation uses `PBKDF2HMAC` with SHA256 hashing for enhanced security.
* Salt is derived from a partial hash of the password for simplicity (consider storing securely for real-world use).

---

## 📂 File Structure

```text
Encryptonator/
├── encryptonator.py          # Main Python script
├── README.md                 # This file
├── .key                      # Key file (generated)
```

---

## 🔒 Disclaimer

This tool is designed for educational and personal use only. Avoid using it for enterprise-level encryption unless modifications are made for secure key storage, salt handling, and audit logging.

---

