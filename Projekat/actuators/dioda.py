import RPi.GPIO as GPIO #Ne moze da se instalira RPi.GPIO
import time


def run_led(pin, delay):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    print("LED on")
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    print("LED off")
    GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()

