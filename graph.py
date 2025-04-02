import csv
import matplotlib.pyplot as plt
from datetime import datetime

dates = []
temperatures = []
humidites = []
conditions = []

def genere_graph_pdf():
    with open("donnees.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            temperatures.append(float(row["temperature"]))
            humidites.append(int(row["humidite"]))
            dates.append(datetime.strptime(row["datetime"], "%Y-%m-%d %H:%M:%S"))

    plt.figure(figsize=(12, 6))

    plt.plot(dates, temperatures, label="Température (°C)", marker="o")
    plt.plot(dates, humidites, label="Humidité", marker="s")

    plt.title("Météo pour les 5 jours à venir") 
    plt.xlabel("Date & Heure")
    plt.ylabel("Valeurs")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graphe.pdf")
    plt.close()
