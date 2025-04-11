from kartenspiel import *
# Testprogramm
spiel = True
kartenstapel = Kartenstapel()
kartenstapel.mischen()
kartenhaufen = Kartenhaufen()
gezogeneKarte = kartenstapel.karteZiehen()


print("___________Blackjack_____________")
if input("Möchtest du spielen? (Ja/Nein)\n") == "Ja":
    print("Hier sind deine Zwei Karten")
    for i in range(2):
        gezogeneKarte = kartenstapel.karteZiehen()
        kartenhaufen.hinzufuegen(gezogeneKarte)
    print(kartenhaufen.kartenListe)
    print(kartenhaufen.wert)
    while spiel:
        if input("Möchtest du eine weitere ziehen oder bei zwei bleiben ? (Hit/Stay)\n") == "Hit":
            gezogeneKarte = kartenstapel.karteZiehen()
            kartenhaufen.hinzufuegen(gezogeneKarte)
            print(kartenhaufen.kartenListe)
            print(kartenhaufen.wert)
            if kartenhaufen.wert > 21:
                print("Du Hast leider Verloren.")
                spiel = False
        else:
            Spiel = False
"""
Schreiben Sie ein Testprogramm, dass Sie 17 und 4 spielen lässt. Nutzereingaben
sollen darüber entscheiden, ob Sie noch eine Karte ziehen oder nicht und benutzer-
freundliche Ausgaben sollen Sie nach jeder gezogenen Karte über ihre Kartenliste sowie
Ihren Kartenwert informieren. Wenn Sie am Ende über 21 Punkte haben, soll
das Programm ausgeben, dass Sie verloren haben.
"""