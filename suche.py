import os
import keyboard  # Stelle sicher, dass du die keyboard-Bibliothek installiert hast

def search_keywords_in_file(file_path, keywords):
    with open(file_path, 'r', encoding='utf-8') as file:
        line_number = 0
        for line in file:
            line_number += 1
            for keyword in keywords:
                if keyword in line:
                    print(f"Zeile {line_number}: {line.strip()}")
                    # Warten auf die "p"-Taste zum Fortfahren
                    while True:
                        if keyboard.is_pressed('p'):
                            print("\nFortfahren...")
                            break

def main():
    file_path = input("Gib den Pfad zur Textdatei ein: ").strip()
    if not os.path.isfile(file_path):
        print("Die angegebene Datei existiert nicht.")
        return

    keywords_input = input("Gib die Suchbegriffe (durch Kommas getrennt) ein: ").strip()
    keywords = [keyword.strip() for keyword in keywords_input.split(',')]

    print("Suche gestartet. Drücke Strg + C, um den Vorgang zu stoppen. Drücke 'p', um zu pausieren.")

    try:
        search_keywords_in_file(file_path, keywords)
    except KeyboardInterrupt:
        print("\nSuche beendet.")
        # Keine "clear" Kommando am Ende, damit die Ergebnisse sichtbar bleiben

if __name__ == "__main__":
    main()
