import time
import random  # Ersetze dies durch den echten Sensorauslesecode

def read_sensor():
    # Simulierte Werte, ersetze dies mit deinem Sensor-Code
    temp = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 60), 2)
    pressure = round(random.uniform(980, 1020), 2)
    
    return f"{temp},{humidity},{pressure}"

while True:
    with open("/var/www/html/data.txt", "w") as file:
        file.write(read_sensor())
    time.sleep(2)
