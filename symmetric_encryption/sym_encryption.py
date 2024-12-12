from cryptography.fernet import Fernet

# Schlüssel generieren
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Text verschlüsseln
text = b"Geheime Nachricht"
encrypted_text = cipher_suite.encrypt(text)
print(f"Verschlüsselt: {encrypted_text}")

# Text entschlüsseln
decrypted_text = cipher_suite.decrypt(encrypted_text)
print(f"Entschlüsselt: {decrypted_text.decode()}")
