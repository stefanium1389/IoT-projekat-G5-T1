import RPi.GPIO as GPIO


def button_print(name):
    print("Button pressed! " + name + "\n")


def button_scan(pin, name):
    PORT_BUTTON = pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PORT_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(PORT_BUTTON, GPIO.RISING, callback=button_print(name), bouncetime=100)

    input("Input any key to continue...")
