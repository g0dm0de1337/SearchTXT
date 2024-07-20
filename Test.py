import os
import sys
import msvcrt

def search_keywords_in_file(file_path, keywords, output_dir):
    # Erstellen eines neuen Ausgabe-Dateinamens
    def get_next_file_name():
        nonlocal file_index
        while True:
            file_name = os.path.join(output_dir, f"treffer{file_index}.txt")
            if not os.path.exists(file_name):
                return file_name
            file_index += 1

    file_index = 1
    output_file_name = get_next_file_name()
    output_file = open(output_file_name, 'w', encoding='utf-8')
    line_number = 0
    hits = 0
    paused = False

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_number += 1
                if paused:
                    print("Gesperrt. Drücke 'p', um fortzufahren...")
                    while paused:
                        if msvcrt.kbhit() and msvcrt.getch().decode() == 'p':
                            paused = False
                            print("Fortgesetzt.")
                            break
                for keyword in keywords:
                    if keyword in line:
                        output_file.write(f"Zeile {line_number}: {line.strip()}\n")
                        hits += 1
                        if hits >= 200:
                            output_file.close()
                            print(f"200 Treffer erreicht. Ergebnis gespeichert in {output_file_name}")
                            file_index += 1
                            output_file_name = get_next_file_name()
                            output_file = open(output_file_name, 'w', encoding='utf-8')
                            hits = 0
                        break
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

    output_dir = input("Gib den Pfad zum Ausgabeverzeichnis ein: ").strip()
    if not os.path.isdir(output_dir):
        print("Das angegebene Verzeichnis existiert nicht.")
        return

    keywords_input = input("Gib die Suchbegriffe (durch Kommas getrennt) ein: ").strip()
    keywords = [keyword.strip() for keyword in keywords_input.split(',')]

    print("Suche gestartet. Drücke 'p', um kurzzeitig zu pausieren, und Strg + C, um den Vorgang zu stoppen.")

    search_keywords_in_file(file_path, keywords, output_dir)

if __name__ == "__main__":
    main()
