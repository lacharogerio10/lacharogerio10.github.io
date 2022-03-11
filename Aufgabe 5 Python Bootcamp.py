print("Hey, mein Name ist Captain Hook und ich will ein Spiel spielen!!!!")
print("Es geht so.Wenn du meine gemeime Zahl errätst, bekommst du einen großen Schatz!!!")
print("Dafür hast du 6 Versuche. Dann wollen wie mal loslegen!!!")

import random
versuche = 5
zufallszahl= random.randint(1,100)
meineZahl = 10
while True:
    print("Versuch duch mal zu Raten!!!!")
    meineZahl= int(input())
    if meineZahl > zufallszahl:
        print("Zu hoch")
        print("Du hast noch " + str(versuche)+ " Versuche übrig.")
        versuche-=1
    if meineZahl < zufallszahl:
        print("Zu niedrig")
        print("Du hast noch " + str(versuche)+ " Versuche übrig.")
        versuche-=1
    if meineZahl == zufallszahl:
        print("Herzlichen Glückwunsch!!!")
        print("Beim nächsten mal wirst du es nicht schaffen!!!!")
        break
    if versuche == -1:
        print("Tja,was soll ich sagen?? Die Zahl war",zufallszahl)
        print("Du hast verloren!!Nächstes Mal wieder!!!")
        break
    
    
