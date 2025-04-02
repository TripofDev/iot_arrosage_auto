# IoT Méteo Automatique & Prévision Météo

Un projet Python simple mais complet qui récupère la météo réelle d’une ville, génère un graphique PDF des prévisions, et l’envoie automatiquement via un bot Telegram.  
Parfait pour simuler une **mini-station météo connectée**.

## Fonctionnement

- Récupère les prévisions météo horaires (température, humidité, description)
- Génère un graphe de suivi météo (`graphe.pdf`)
- Sauvegarde les données dans un fichier `donnees.csv`
- Envoie le graphe chaque matin via Telegram à 8h


## BESOIN

Python
Compte sur OpenWeatherMap
Compte Telegram
Librairies : requests, matplotlib
```
pip install requests matplotlib
```

## Lancement
```shell
git clone https://github.com/votre-utilisateur/iot_arrosage_auto.git
```
```shell
cd https://github.com/votre-utilisateur/iot_arrosage_auto.git
```

Remplacez :
```env
API_KEY = "votre_clé_openweathermap"
BOT_TOKEN = "votre_token_telegram"
VILLE = "ta_ville"
CHAT_ID = "votre_id_chat"
```
Par vos clé ou tokken respectif et par le nom de la ville dont vous souhaitez la météo puis faites
```
python meteo.py
```
Vous devriez recevoir une notification sur telegram avec le pdf de la prévision météo


## En Cours

Le mettre sur un Raspberry avec un serveur local pour pouvoir en faire un crontab qui tourne tout les jours sans avoir à lancer le script manuellement
