import bcrypt  # Importiert die bcrypt-Bibliothek, um Passwörter sicher zu hashen und zu überprüfen

# Passwort, das gehasht werden soll (als Bytes, da bcrypt mit Bytes arbeitet)
password = b"mein_sicheres_passwort"

# Generiert einen sicheren Hash für das Passwort mit einem zufälligen Salt
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(f"Passwort-Hash: {hashed}")  # Gibt den generierten Hash aus

# Überprüft, ob das ursprüngliche Passwort mit dem generierten Hash übereinstimmt
if bcrypt.checkpw(password, hashed):  # Prüft das Passwort gegen den Hash
    print("Passwort ist korrekt!")  # Gibt aus, wenn das Passwort korrekt ist
else:
    print("Falsches Passwort!")  # Gibt aus, wenn das Passwort nicht übereinstimmt
