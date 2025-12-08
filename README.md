# A simple but complete Python project that retrieves real weather data from a city, generates a PDF chart of forecasts, and automatically sends it via a Telegram bot.  
Perfect for simulating a **connected mini weather station**.atic IoT Weather & Weather Forecast

A simple but complete Python project that retrieves real weather data from a city, generates a PDF chart of forecasts, and automatically sends it via a Telegram bot.  
Perfect for simulating a **connected mini weather station**.T Méteo Automatique & Prévision Météo

Un projet Python simple mais complet qui récupère la météo réelle d’une ville, génère un graphique PDF des prévisions, et l’envoie automatiquement via un bot Telegram.  
Parfait pour simuler une **mini-station météo connectée**.

## How It Works

- Retrieves hourly weather forecasts (temperature, humidity, description)
- Generates a weather tracking graph (`graphe.pdf`)
- Saves data in a `donnees.csv` file
- Sends the graph every morning via Telegram at 8 AM


## Requirements

- Python
- OpenWeatherMap account
- Telegram account
- Libraries: requests, matplotlib

```bash
pip install requests matplotlib
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/your-username/iot_arrosage_auto.git
```

Navigate to the project directory:

```bash
cd iot_arrosage_auto
```

Replace the following values with your own:

```env
API_KEY = "your_openweathermap_key"
BOT_TOKEN = "your_telegram_token"
VILLE = "your_city"
CHAT_ID = "your_chat_id"
```

Then run the script:

```bash
python meteo.py
```

You should receive a notification on Telegram with the weather forecast PDF.


## In Progress

Deploy on a Raspberry Pi with a local server to set up a crontab that runs daily without having to manually launch the script.
