import os
import keyboard  # Für Tasteneingaben
import time  # Für Pausen in der Schleife

def search_keywords_in_file(file_path, keywords):
    line_number = 0
    hits = 0
    paused = False

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_number += 1
                
                # Überprüfen, ob 'p' gedrückt wurde, um zu pausieren
                if keyboard.is_pressed('p'):
                    paused = not paused
                    if paused:
                        print("Pause aktiviert. Drücke 'p', um fortzufahren.")
                    while paused:
                        time.sleep(0.1)  # Kurze Pause zur Vermeidung von CPU-Überlastung
                        if keyboard.is_pressed('p'):
                            paused = False
                            print("Fortgesetzt.")
                            break
                
                if paused:
                    continue

                for keyword in keywords:
                    if keyword in line:
                        print(f"Zeile {line_number}: {line.strip()}")
                        hits += 1
                        break

    except KeyboardInterrupt:
        print("\nSuche beendet.")

def main():
    file_path = input("Gib den Pfad zur Textdatei ein: ").strip()
    if not os.path.isfile(file_path):
        print("Die angegebene Datei existiert nicht.")
        return

    keywords_input = input("Gib die Suchbegriffe (durch Kommas getrennt) ein: ").strip()
    keywords = [keyword.strip() for keyword in keywords_input.split(',')]

    print("Suche gestartet. Drücke 'p', um die Live-Ergebnisse zu pausieren oder fortzusetzen, und Strg + C, um den Vorgang zu stoppen.")

    search_keywords_in_file(file_path, keywords)

if __name__ == "__main__":
    main()
