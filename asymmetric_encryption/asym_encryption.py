# Importiert die notwendigen Module und Klassen für die asymmetrische Verschlüsselung und Hashing
from cryptography.hazmat.primitives.asymmetric import rsa, padding  # Für RSA und Padding-Schema
from cryptography.hazmat.primitives import hashes  # Für die Hash-Algorithmen (z. B. SHA256)

# Schlüsselpaar generieren: Erstellt einen privaten Schlüssel (RSA) mit einer Schlüssellänge von 2048 Bit
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Standardwert für den öffentlichen Exponenten (sicher und üblich)
    key_size=2048  # Die Größe des Schlüssels in Bits (2048 ist eine sichere Länge)
)

# Extrahiert den öffentlichen Schlüssel aus dem privaten Schlüssel
public_key = private_key.public_key()

# Nachricht definieren: Die zu verschlüsselnde Nachricht als Byte-String
message = b"Geheime Nachricht"  # Nachricht, die verschlüsselt werden soll (als Bytes, da RSA mit Bytes arbeitet)

# Verschlüsselt die Nachricht mit dem öffentlichen Schlüssel
encrypted = public_key.encrypt(
    message,  # Die zu verschlüsselnde Nachricht
    padding.OAEP(  # Verwendet das OAEP-Padding-Schema für zusätzliche Sicherheit
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask-Generating Function (MGF1) mit SHA256
        algorithm=hashes.SHA256(),  # Hash-Algorithmus für das Padding
        label=None  # Optionale Label-Informationen (hier nicht verwendet)
    )
)
print(f"Verschlüsselt: {encrypted}")  # Gibt die verschlüsselte Nachricht aus (als Bytes)

# Entschlüsselt die verschlüsselte Nachricht mit dem privaten Schlüssel
decrypted = private_key.decrypt(
    encrypted,  # Die verschlüsselte Nachricht
    padding.OAEP(  # Verwendet das gleiche OAEP-Padding-Schema wie bei der Verschlüsselung
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask-Generating Function (MGF1) mit SHA256
        algorithm=hashes.SHA256(),  # Hash-Algorithmus für das Padding
        label=None  # Label-Informationen müssen identisch mit der Verschlüsselung sein (hier None)
    )
)
# Gibt die entschlüsselte Nachricht aus, indem die Byte-Daten in einen lesbaren String konvertiert werden
print(f"Entschlüsselt: {decrypted.decode()}")  # Decodiert die Byte-Daten zurück in einen lesbaren String
