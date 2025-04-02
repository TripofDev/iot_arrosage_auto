import requests
from datetime import datetime
import csv
from graph import genere_graph_pdf
from send_bot import envoyer_pdf_telegram

API_KEY = "YOUR_API_KEY_OF_OPENWEATHERMAP"
VILLE = "YOUR_CITY"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={VILLE}&appid={API_KEY}&units=metric&lang=fr"

def get_previsions():
    response = requests.get(URL)
    data = response.json()

    if response.status_code != 200:
        print("❌ Erreur API :", data)
        return []

    previsions = []
    for item in data["list"]:
        dt_txt = item["dt_txt"]
        temp = item["main"]["temp"]
        humidite = item["main"]["humidity"]
        desc = item["weather"][0]["description"]

        previsions.append({
            "datetime": dt_txt,
            "temperature": temp,
            "humidite": humidite,
            "description": desc
        })

    return previsions

def enregistrer_previsions_csv(previsions):
    with open("donnees.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["datetime", "temperature", "humidite", "description"])
        for p in previsions:
            writer.writerow([p["datetime"], p["temperature"], p["humidite"], p["description"]])


if __name__ == "__main__":
    previsions = get_previsions()
    enregistrer_previsions_csv(previsions)
    genere_graph_pdf()
    envoyer_pdf_telegram()