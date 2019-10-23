import msvcrt
print("""Witaj w programie do... wylaczenia programu!
Naciśnij spacje, by wylaczyc program""")
while not msvcrt.getch() == b' ':
        print("To nie ten przycisk")
