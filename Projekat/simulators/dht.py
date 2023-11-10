import time
import random


def generate_value(initial_temp=25, initial_humidity=20):
    temperature = initial_temp
    humidity = initial_humidity

    temperature = temperature + random.randint(-1, 1)
    humidity = humidity + random.randint(-1, 1)

    return humidity, temperature

    # while True:
    #       temperature = temperature + random.randint(-1, 1)
    #       humidity = humidity + random.randint(-1, 1)
    #       if humidity < 0:
    #             humidity = 0
    #       if humidity > 100:
    #             humidity = 100
    #       yield humidity, temperature


def run_dht_simulator(delay, callback): #stop_event):
    # for h, t in generate_value():
    h, t = generate_value()
    time.sleep(delay)  # Delay between readings (adjust as needed)
    callback(h, t, "RDHT1")
    # if stop_event.is_set():
    #     break
