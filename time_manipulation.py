import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def horloge():
    a = True
    print("entrez n'importe qui pour arreter l'horloge. appuyer sur 'entrée' pour renouveller l'heure")
    while a:
        y = str(datetime.now())
        print(f"    {y}", end="\r")
        time.sleep(0.1)
        print("", end="\r")
        time.sleep(0.1)
        if input() != "":
            a = False

def chronometre(name):
    z = True
    print("entrez n'importe qui pour arreter le  chronometre. appuyez sur 'entrée' pour renouveller le chnonometre.")
    while z:
        H = datetime.now()
        C = H - name
        print(f"    temps ecoulé : {C}", end="\r")
        if input() != "":
            z = False
        time.sleep(0.1)

def minuteur():
    a = True
    print("pou connaitre le temps qui reste, appyez sur 'entrée'. pou sortir appyez sur n'importe quoi.")
    z = int(input("ce minuteur doit attendre combien de secondes ? "))
    H = datetime.now() + timedelta(seconds=z)
    while a:
        U = H - datetime.now()
        if U.total_seconds() <= 0:
            print("temps écoulé.")
        else:
            print(f"    {U}", end="\r") 
        if input() != "":
            a = False
        if U.total_seconds() <= 0:
            a = False

def intervalle_entre_deux_periodes():
    print("entrez l'annee, le jour, le mois.")
    A1 = int(input("annee : "))
    M1 = int(input("mois : "))
    J1 = int(input("jour : "))
    Date_1 = datetime(A1, M1, J1)
    print(f"la premire date est : {Date_1.strftime("%d/%m/%Y")}")

    print("entrez l'annee, le jour, le mois de la deuxieme date.")
    A2 = int(input("annee : "))
    M2 = int(input("mois : "))
    J2 = int(input("jour : "))
    Date_2 = datetime(A2, M2, J2)
    print(f"la premire date est : {Date_2.strftime("%d/%m/%Y")}")
    
    date = relativedelta(Date_1, Date_2)
    print(f"l'intervalle est de  : {date.years} annees, {date.months} mois, et {date.days} jours.")


def intervalle_une_periode_aujourdhui():
    print("entrez l'annee, le jour, le mois.")
    A1 = int(input("annee : "))
    M1 = int(input("mois : "))
    J1 = int(input("jour : "))
    Date_1 = datetime(A1, M1, J1)
    print(f"la premire date est : {Date_1.strftime("%d/%m/%Y")}")

    Date_2 = datetime.now()
    print(f"la premire date est : {Date_2.strftime("%d/%m/%Y")}")
    
    date = relativedelta(Date_2, Date_1)
    print(f"l'intervalle est de  : {date.years} annees, {date.months} mois, et {date.days} jours.")

print("")
e = True
while e:
    print("bienvenue dans ce programme qui gères le temps.")
    q = True
    while q:
        x = input("que voulez vous faire ? connaitre l'heure(a), utiliser un chronmetre(b) ou minuteur (c), calculer l'interval entre 2 dates(d) ou entre une date et aujourd'hui (e): ")
        if isinstance(x, str):
            x = x.lower()
            if x in ["a", "b", "c", "d", "e"]:
                q = False
    if x == "a":
        horloge()
    elif x == "b":
        current_time = datetime.now()
        chronometre(current_time)
    elif x == "c":
        minuteur()
    elif x == "d":
        intervalle_entre_deux_periodes()
    else:
        intervalle_une_periode_aujourdhui()
    
    s = input("voulez vous essayer d'autres fonctionnalitees de ce programme (oui/non) ? ")
    if isinstance(s, str):
        if s.lower() == "oui":
            e = True
        else:
            e = False

    print("")