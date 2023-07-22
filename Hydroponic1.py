import time
import Adafruit_DHT
import RPi.GPIO as GPIO

# Sensor and Actuator Configuration
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 17  # GPIO pin where DHT11 data pin is connected
WATER_LEVEL_PIN = 18  # GPIO pin where water level sensor is connected
WATER_PUMP_PIN = 27  # GPIO pin where water pump relay is connected

# Threshold for turning on the water pump (example value)
WATER_LEVEL_THRESHOLD = 30  # Adjust this value based on your setup

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(WATER_LEVEL_PIN, GPIO.IN)
GPIO.setup(WATER_PUMP_PIN, GPIO.OUT)

def read_dht_sensor():
    # Read temperature and humidity from DHT11 sensor
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return round(temperature, 2), round(humidity, 2)
    else:
        return None, None

def read_water_level():
    # Read water level sensor data (example: 0 - water present, 1 - water absent)
    return GPIO.input(WATER_LEVEL_PIN)

def control_water_pump(status):
    # Control water pump based on the status (True - ON, False - OFF)
    GPIO.output(WATER_PUMP_PIN, status)

try:
    while True:
        # Read sensor data
        temperature, humidity = read_dht_sensor()
        water_level = read_water_level()

        # Print sensor data
        if temperature is not None and humidity is not None:
            print(f"Temperature: {temperature} °C, Humidity: {humidity}%")
        else:
            print("Failed to retrieve DHT11 sensor data.")

        # Control water pump based on water level
        if water_level == 0:
            print("Water level is normal.")
            control_water_pump(False)  # Turn off the water pump
        else:
            print("Water level is low. Turning on the water pump.")
            control_water_pump(True)   # Turn on the water pump

        print("------------------------")
        time.sleep(5)  # 5 seconds delay between readings

except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Cleanup GPIO configuration
    GPIO.cleanup()
