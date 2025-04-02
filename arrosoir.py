import random
import time
import csv
import os
from datetime import datetime

historique_temp = []
historique_humidite = []
historique_lumiere = []

def genere_temp():
    return random.randint(1,40)

def afficher_rapport_temp():
    if len(historique_temp) >= 5:
        max_temp = max(historique_temp)
        min_temp = min(historique_temp)
        moyenne = sum(historique_temp) / len(historique_temp)
        print(f"\n--- Rapport ---")
        print(f"Températures enregistrées : {historique_temp}")
        print(f"🌡️ Moyenne : {moyenne}°C | 🔺 Max : {max_temp}°C | 🔻 Min : {min_temp}°C")
        print(f"--- Fin du rapport ---\n")

def genere_humidite():
    return random.randint(0,1)

def afficher_rapport_humidite():
    if len(historique_humidite) >= 5:
        max_lumiere = max(historique_humidite)
        min_lumiere = min(historique_humidite)
        moyenne = sum(historique_humidite) / len(historique_humidite)
        print(f"\n--- Rapport ---")
        print(f"Températures enregistrées : {historique_humidite}")
        print(f"🌡️ Moyenne : {moyenne}°C | 🔺 Max : {max_lumiere}°C | 🔻 Min : {min_lumiere} SWI")
        print(f"--- Fin du rapport ---\n")

def genere_luminosité():
    return random.randint(0,99)

def afficher_rapport_lumiere():
    if len(historique_lumiere) >= 5:
        max_humidite = max(historique_lumiere)
        min_humidite = min(historique_lumiere)
        moyenne = sum(historique_lumiere) / len(historique_lumiere)
        print(f"\n--- Rapport ---")
        print(f"lumiere enregistrées : {historique_lumiere}")
        print(f"🌡️ Moyenne : {moyenne}°C | 🔺 Max : {max_humidite}°C | 🔻 Min : {min_humidite} lm")
        print(f"--- Fin du rapport ---\n")



def enregistrer_csv(temp, humid, lumiere):
    fichier = "donnees.csv"
    fichier_existe = os.path.exists(fichier)
    
    with open(fichier, "a", newline="") as f:
        writer = csv.writer(f)
        if not fichier_existe:
            writer.writerow(["datetime", "temperature", "humidite", "luminosite"])
            maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([maintenant, temp, humid, lumiere])

while (True):
    temp = genere_temp()
    humid = genere_humidite()
    lumiere = genere_luminosité()
    date_jour = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    historique_temp.append(temp)
    historique_humidite.append(humid)
    historique_lumiere.append(lumiere)

    afficher_rapport_temp()
    afficher_rapport_humidite()
    afficher_rapport_lumiere()

    enregistrer_csv(temp, humid, lumiere)
    
    if temp < 20:
        print(f"la temperature est de {temp} , l'arrosage sera de 2 par jour")
    elif temp > 30:
        print(f"la temperature est de {temp} , l'arrosage sera de 4 par jour")
    else:
        print(f"la temperature est de {temp} , l'arrosage sera de 3 par jour")

    if temp >= 35:
        print(f"Alerte ! Température critique : {temp}°C")

    time.sleep(2)
