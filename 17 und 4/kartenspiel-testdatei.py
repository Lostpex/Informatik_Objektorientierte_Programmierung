from kartenspiel import *
# Testprogramm

kartenstapel = Kartenstapel()

kartenstapel.mischen()
print(kartenstapel.kartenListe)
print()
kartenhaufen = Kartenhaufen()
gezogeneKarte = kartenstapel.karteZiehen()
kartenhaufen.hinzufuegen(gezogeneKarte)
print(kartenhaufen.kartenListe)
print(kartenstapel.kartenListe)
print(kartenhaufen.wert)

"""
Schreiben Sie ein Testprogramm, dass Sie 17 und 4 spielen lässt. Nutzereingaben
sollen darüber entscheiden, ob Sie noch eine Karte ziehen oder nicht und benutzer-
freundliche Ausgaben sollen Sie nach jeder gezogenen Karte über ihre Kartenliste sowie
Ihren Kartenwert informieren. Wenn Sie am Ende über 21 Punkte haben, soll
das Programm ausgeben, dass Sie verloren haben.
"""