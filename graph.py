import csv
import matplotlib.pyplot as plt
from datetime import datetime

dates = []
temperatures = []
humidites = []
lumieres = []

def genere_graph_pdf():
    with open("donnees.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            temperatures.append(int(row["temperature"]))
            humidites.append(int(row["humidite"]))
            lumieres.append(int(row["luminosite"]))
            dates.append(datetime.strptime(row["datetime"], "%Y-%m-%d %H:%M:%S"))

    plt.figure(figsize=(12, 6))

    plt.plot(dates, temperatures, label="Température (°C)", marker="o")
    plt.plot(dates, humidites, label="Humidité", marker="s")
    plt.plot(dates, lumieres, label="Luminosité", marker="^")

    plt.title("📊 Suivi environnemental complet")
    plt.xlabel("Date & Heure")
    plt.ylabel("Valeurs")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graphe.pdf")
    plt.close()
