import bcrypt

# Passwort-Hashen
password = b"mein_sicheres_passwort"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(f"Passwort-Hash: {hashed}")

# Passwortüberprüfung
if bcrypt.checkpw(password, hashed):
    print("Passwort ist korrekt!")
else:
    print("Falsches Passwort!")
