import requests
from datetime import datetime
import time
from graph import genere_graph_pdf

TOKEN = "YOUR_CHAT_ID"
TOKEN_BOT = "Your_Telegram_Bot_Token"

horaire_actuel = datetime.now().strftime("%H:%M:%S")
horaire_needed = ("08:00:00")

def envoyer_pdf_telegram(token_bot, chat_id, chemin_fichier):
    url = f"https://api.telegram.org/bot{token_bot}/sendDocument"
    with open(chemin_fichier, "rb") as fichier:
        data = {"chat_id": chat_id}
        files = {"document": fichier}
        response = requests.post(url, data=data, files=files)
    return response

while True:
    heure = datetime.now().strftime("%H:%M:%S")
    if heure == "08:00:00":
        genere_graph_pdf()
        envoyer_pdf_telegram(TOKEN_BOT, TOKEN, "graphe.pdf")
        print("✅ Fichier envoyé !")
        time.sleep(61)
    else:
        time.sleep(1)
