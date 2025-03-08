import time
import mysql.connector
import board
import adafruit_dht

# Initialisieren Sie das dht-Gerät, wobei der Datenpin mit Pin 16 (GPIO 23) des Raspberry Pi verbunden ist:
#dhtDevice = adafruit_dht.DHT11(board.D23)

# Sie können DHT22 use_pulseio=False übergeben, wenn Sie pulseio nicht verwenden möchten.
# Dies kann auf einem Linux-Einplatinencomputer wie dem Raspberry Pi notwendig sein,
# aber es wird nicht in CircuitPython funktionieren.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

db_config = {
    "host": "localhost",  # Oder "localhost", falls lokal
    "user": "piproject",
    "password": "123456",
    "database": "piproject"
}

def insert_data(temp_c, temp_f, humidity):
    """Fügt Messwerte in die Datenbank ein"""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        sql = "INSERT INTO measurements (temperature_c, temperature_f, humidity) VALUES (%s, %s, %s)"
        cursor.execute(sql, (temp_c, temp_f, humidity))
        conn.commit()
        print(f"Eingefügt: {temp_c}°C, {temp_f}°F, {humidity}% Luftfeuchte")
    except mysql.connector.Error as err:
        print(f"Datenbankfehler: {err}")
    finally:
        cursor.close()
        conn.close()

insert_data(55, 56, 3)

while True:
    try:
        # Drucken der Werte über die serielle Schnittstelle
        #temperature_c = dhtDevice.temperature
        #temperature_f = temperature_c * (9 / 5) + 32
        #humidity = dhtDevice.humidity
        temperature_c = 24
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = 86
        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))

    except RuntimeError as error:
        # Fehler passieren ziemlich oft, DHT's sind schwer zu lesen, einfach weitermachen
        print(error.args[0])
        time.sleep(2.0)
        continue
    #except Exception as error:
        #dhtDevice.exit()
        #raise error

    time.sleep(2.0)
