import time

print("🎰 Willkommen beim erweiterten Lottospiel! 🎰")

# Geldeinsatz
einsatz = float(input("Bitte geben Sie Ihren Einsatz in Euro ein: "))

# Benutzereingabe für Lottozahlen
print("Bitte geben Sie Ihre 6 Lottozahlen zwischen 1 und 49 ein.")
benutzerzahlen = []
i = 0
while i < 6:
    zahl = int(input(f"Zahl {i+1}: "))
    if 1 <= zahl <= 49 and zahl not in benutzerzahlen:
        benutzerzahlen.append(zahl)
        i += 1
    else:
        print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 49 wählen, die noch nicht gewählt wurde.")

# Benutzereingabe für Superzahl
benutzer_superzahl = int(input("Bitte geben Sie Ihre Superzahl zwischen 0 und 9 ein: "))
while benutzer_superzahl < 0 or benutzer_superzahl > 9:
    benutzer_superzahl = int(input("Bitte geben Sie Ihre Superzahl zwischen 0 und 9 ein: "))

# Eigene Zufallszahlengenerierung
def eigener_zufall(max_wert):
    time.sleep(0.01)  # Kleine Verzögerung
    return int((time.time() * 1000000) % max_wert) + 1

# Ziehung der Lottozahlen und Superzahl
gewinnzahlen = []
while len(gewinnzahlen) < 6:
    zahl = eigener_zufall(49)
    if zahl not in gewinnzahlen:
        gewinnzahlen.append(zahl)
superzahl = eigener_zufall(10) - 1

# Vergleich und Auswertung
richtige = []
for zahl in benutzerzahlen:
    if zahl in gewinnzahlen:
        richtige.append(zahl)
anzahl_richtige = len(richtige)
superzahl_richtig = benutzer_superzahl == superzahl

# Ergebnisausgabe
print("🎉 Die Ziehung ist abgeschlossen! 🎉")
print(f"Ihre Zahlen: {benutzerzahlen} - Superzahl: {benutzer_superzahl}")
print(f"Gewinnzahlen: {gewinnzahlen} - Superzahl: {superzahl}")
print(f"Sie haben {anzahl_richtige} richtige Zahl(en):")
if anzahl_richtige > 0:
     print(f"Richtige Zahlen: {richtige}")

if superzahl_richtig:
    print("🌟 Sie haben die richtige Superzahl!")

# Gewinnauswertung
gewinn = 0
if anzahl_richtige == 6 and superzahl_richtig:
    gewinn = einsatz * 1000000
    print(f"🏆 JACKPOT! Sie haben alle Zahlen und die Superzahl richtig! Gewinn: {gewinn:.2f} €")
elif anzahl_richtige == 6:
    gewinn = einsatz * 100000
    print(f"🎈 Fantastisch! Sie haben alle 6 Zahlen richtig! Gewinn: {gewinn:.2f} €")
elif anzahl_richtige == 5 and superzahl_richtig:
    gewinn = einsatz * 10000
    print(f"🎊 Großartig! 5 Richtige und die Superzahl! Gewinn: {gewinn:.2f} €")
elif anzahl_richtige == 5:
    gewinn = einsatz * 1000
    print(f"🎉 Super! Sie haben 5 Richtige! Gewinn: {gewinn:.2f} €")
elif anzahl_richtige == 4:
    gewinn = einsatz * 100
    print(f"👍 Gut gemacht! 4 Richtige! Gewinn: {gewinn:.2f} €")
elif anzahl_richtige == 3:
    gewinn = einsatz * 10
    print(f"😊 Nicht schlecht! 3 Richtige! Gewinn: {gewinn:.2f} €")
else:
    print(f"😔 Leider kein Gewinn. Sie haben Ihren Einsatz von {einsatz:.2f} € verloren.")

# Gewinnwahrscheinlichkeiten
print("📊 Gewinnwahrscheinlichkeiten:")
print("6 Richtige + Superzahl: 1 zu 15537573")
print("6 Richtige: 1 zu 13983816")
print("5 Richtige + Superzahl: 1 zu 542008")
print("5 Richtige: 1 zu 60096")
print("4 Richtige: 1 zu 1032")
print("3 Richtige: 1 zu 57")

print("🍀 Vielen Dank fürs Spielen! Möge das Glück mit Ihnen sein! 🍀")
