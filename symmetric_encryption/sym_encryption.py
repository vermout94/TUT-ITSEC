# Importiert die Fernet-Klasse für symmetrische Verschlüsselung aus der cryptography-Bibliothek
from cryptography.fernet import Fernet

# Schlüssel generieren: Erstellt einen zufälligen Schlüssel für die symmetrische Verschlüsselung
key = Fernet.generate_key()  # Der Schlüssel ist eine sichere Basis64-kodierte Bytefolge
cipher_suite = Fernet(key)  # Erstellt ein Fernet-Objekt mit dem generierten Schlüssel

# Text definieren: Die zu verschlüsselnde Nachricht als Byte-String
text = b"Geheime Nachricht"  # Nachricht, die verschlüsselt werden soll (als Bytes, da Fernet mit Bytes arbeitet)

# Verschlüsselt die Nachricht mit dem Fernet-Schlüssel
encrypted_text = cipher_suite.encrypt(text)  # Die Nachricht wird sicher verschlüsselt
print(f"Verschlüsselt: {encrypted_text}")  # Gibt die verschlüsselte Nachricht aus (als Bytes)

# Entschlüsselt die verschlüsselte Nachricht mit dem Fernet-Schlüssel
decrypted_text = cipher_suite.decrypt(encrypted_text)  # Die verschlüsselte Nachricht wird entschlüsselt
print(f"Entschlüsselt: {decrypted_text.decode()}")  # Decodiert die Byte-Daten zurück in einen lesbaren String
