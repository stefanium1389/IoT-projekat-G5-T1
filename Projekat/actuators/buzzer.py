import RPi.GPIO as GPIO
import time

def buzzer_buzz(pin, delay):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    print("Start buzz")
    GPIO.output(pin, True)
    time.sleep(delay)
    print("Stop buzz")
    GPIO.output(pin, False)
    time.sleep(delay)

