import RPi.GPIO as GPIO


def pir_print(name):
    print("Motion detected! " + name + "\n")


def pir_scan(pin, name):
    PIR_PIN = pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN)

    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=pir_print(name))

    input("Input any key to continue...")
