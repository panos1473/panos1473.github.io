import requests
import random
import time

CHANNEL_ID = "2573245"
API_KEY = "X0HE7FEFED68VZ7W"

def send_data_to_thingspeak(temperature, soil_moisture, water_pressure):
    url = f"https://api.thingspeak.com/update?api_key=X0HE7FEFED68VZ7W&field1={temperature}&field2={soil_moisture}&field3={water_pressure}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Τα δεδομένα στάλθηκαν επιτυχώς στο ThingSpeak")
    else:
        print("Σφάλμα κατά την αποστολή δεδομένων στο ThingSpeak")


while True:
    temperature = random.randint(28, 50)
    soil_moisture = random.randint(0, 100)
    water_pressure = random.randint(0, 100)
    send_data_to_thingspeak(temperature, soil_moisture, water_pressure)
    time.sleep(15)
