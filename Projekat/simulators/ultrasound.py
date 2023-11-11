import time
import random

def generate_value(initial_distance=7, flux = 3):
    distance = initial_distance
    distance = distance + random.randint(-flux, flux)
    return distance

def run_ultrasound_simulation():
    d = generate_value()
    time.sleep(1)
    return d