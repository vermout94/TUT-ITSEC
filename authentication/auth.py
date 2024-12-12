import getpass

# Benutzer und Passwörter speichern
users = {"admin": "securepassword", "user": "mypassword"}

# Authentifizierung
username = input("Benutzername: ")
password = getpass.getpass("Passwort: ")

if username in users and users[username] == password:
    print(f"Willkommen, {username}!")
else:
    print("Ungültige Anmeldedaten.")

# Autorisierung
if username == "admin":
    print("Sie haben Zugriff auf administrative Ressourcen.")
else:
    print("Sie haben nur Benutzerzugriff.")
