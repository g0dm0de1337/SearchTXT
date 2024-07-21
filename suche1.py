import os
import keyboard  # Für Tasteneingaben
import time  # Für Pausen in der Schleife

def search_keywords_in_file(file_path, keywords, output_dir):
    line_number = 0
    hits = 0
    file_index = 1
    max_hits_per_file = 1500
    paused = False
    output_file_name = os.path.join(output_dir, f"treffer{file_index}.txt")
    output_file = open(output_file_name, 'w', encoding='utf-8')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_number += 1
                
                # Überprüfen, ob 'p' gedrückt wurde, um zu pausieren
                if keyboard.is_pressed('p'):
                    paused = True
                    print("Pause aktiviert. Drücke 'w', um fortzufahren.")
                    while paused:
                        time.sleep(0.1)  # Kurze Pause zur Vermeidung von CPU-Überlastung
                        if keyboard.is_pressed('w'):
                            paused = False
                            print("Fortgesetzt.")
                            break

                if paused:
                    continue
                
                matched = False
                for keyword in keywords:
                    if keyword in line:
                        output_file.write(f"Zeile {line_number}: {line.strip()}\n")
                        hits += 1
                        matched = True
                        break
                
                if hits >= max_hits_per_file:
                    output_file.close()
                    print(f"{max_hits_per_file} Treffer erreicht. Ergebnis gespeichert in {output_file_name}")
                    file_index += 1
                    output_file_name = os.path.join(output_dir, f"treffer{file_index}.txt")
                    output_file = open(output_file_name, 'w', encoding='utf-8')
                    hits = 0
                
    except KeyboardInterrupt:
        print("\nSuche beendet.")
    finally:
        output_file.close()
        if hits > 0:
            print(f"Ergebnisse gespeichert in {output_file_name}")

def main():
    file_path = input("Gib den Pfad zur Textdatei ein: ").strip()
    if not os.path.isfile(file_path):
        print("Die angegebene Datei existiert nicht.")
        return

    keywords_input = input("Gib die Suchbegriffe (durch Kommas getrennt) ein: ").strip()
    keywords = [keyword.strip() for keyword in keywords_input.split(',')]

    output_dir = os.path.join(os.path.dirname(file_path), *keywords)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("Suche gestartet. Drücke 'p', um die Live-Ergebnisse zu pausieren, und 'w', um fortzufahren. Drücke Strg + C, um den Vorgang zu stoppen.")

    search_keywords_in_file(file_path, keywords, output_dir)

if __name__ == "__main__":
    main()
