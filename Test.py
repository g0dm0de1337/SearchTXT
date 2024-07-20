import msvcrt

print("Drücke eine Taste...")
char = msvcrt.getch()
print(f"Du hast die Taste '{char.decode()}' gedrückt.")
