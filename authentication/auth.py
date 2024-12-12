import getpass  # Importiert das Modul getpass, um sicher Benutzereingaben (z. B. Passwörter) ohne Anzeige im Terminal abzurufen

# Benutzer und Passwörter speichern (in einem Dictionary, wobei der Benutzername der Schlüssel und das Passwort der Wert ist)
users = {"admin": "securepassword", "user": "mypassword"}

# Authentifizierung: Fragt den Benutzer nach seinem Benutzernamen
username = input("Benutzername: ")  # Liest den Benutzernamen von der Eingabezeile ein

# Fragt den Benutzer nach seinem Passwort, das während der Eingabe nicht angezeigt wird
password = getpass.getpass("Passwort: ")  # Liest das Passwort sicher ein (versteckte Eingabe)

# Überprüft, ob der Benutzername im Dictionary vorhanden ist und ob das eingegebene Passwort mit dem gespeicherten übereinstimmt
if username in users and users[username] == password:
    print(f"Willkommen, {username}!")  # Gibt eine Willkommensnachricht aus, wenn die Anmeldedaten korrekt sind
else:
    print("Ungültige Anmeldedaten.")  # Gibt eine Fehlermeldung aus, wenn die Anmeldedaten nicht korrekt sind

# Autorisierung: Überprüft, ob der Benutzer "admin" ist, um Zugriff auf zusätzliche Ressourcen zu gewähren
if username == "admin":  # Prüft, ob der Benutzername "admin" ist
    print("Sie haben Zugriff auf administrative Ressourcen.")  # Gibt eine Nachricht aus, wenn der Benutzer Admin-Rechte hat
else:
    print("Sie haben nur Benutzerzugriff.")  # Gibt eine Nachricht aus, wenn der Benutzer nur Standardrechte hat
