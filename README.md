# 🚀 Flask Blog App

Dies ist eine einfache, funktionale Blog-Anwendung, die mit dem **Flask-Framework** in Python erstellt wurde. Das Projekt ermöglicht das Erstellen, Lesen, Bearbeiten und Löschen von Blogbeiträgen (CRUD-Funktionalität) sowie eine interaktive "Like"-Funktion.

## ✨ Funktionen (Features)
* **Anzeigen:** Alle Blogbeiträge werden auf der Startseite aus einer JSON-Datei geladen.
* **Hinzufügen:** Neue Beiträge können über ein Formular erstellt werden.
* **Bearbeiten:** Bestehende Beiträge können dynamisch aktualisiert werden.
* **Löschen:** Beiträge können mit einer Bestätigungsabfrage entfernt werden.
* **Bonus - Like-System:** Nutzer können Beiträge mit einem Klick auf das "Like"-Icon unterstützen.
* **Persistenz:** Alle Daten werden dauerhaft in einer `blog.json` Datei gespeichert.

## 🛠️ Technologien (Tech Stack)
* **Backend:** Python 3 & Flask
* **Frontend:** HTML5, CSS3 (Modernes & Responsives Design)
* **Datenformat:** JSON (JavaScript Object Notation)
* **Versionsverwaltung:** Git & GitHub

## 🚀 Installation & Ausführung (Lokal ausführen)

Befolgen Sie diese Schritte, um das Projekt auf Ihrem lokalen Rechner auszuführen:

1.  **Repository klonen:**
    ```bash
    git clone [https://github.com/merwebattal-hue/meine-flask-blog-app.git](https://github.com/merwebattal-hue/meine-flask-blog-app.git)
    cd meine-flask-blog-app
    ```

2.  **Virtuelle Umgebung erstellen (Optional aber empfohlen):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Für Mac/Linux
    # .venv\Scripts\activate   # Für Windows
    ```

3.  **Flask installieren:**
    ```bash
    pip install flask
    ```

4.  **Anwendung starten:**
    ```bash
    python3 app.py
    ```

5.  **Im Browser öffnen:**
    Gehen Sie zu `http://127.0.0.1:5000`

---
*Erstellt von Merve Battal - 2024*
