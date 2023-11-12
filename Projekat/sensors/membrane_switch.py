import RPi.GPIO as GPIO
import time


def membrane_switch_scan(pins):
    # these GPIO pins are connected to the keypad
    # change these according to your connections!
    R1 = pins["R1"]
    R2 = pins["R2"]
    R3 = pins["R3"]
    R4 = pins["R4"]

    C1 = pins["C1"]
    C2 = pins["C2"]
    C3 = pins["C3"]
    C4 = pins["C4"]

    # Initialize the GPIO pins

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(R1, GPIO.OUT)
    GPIO.setup(R2, GPIO.OUT)
    GPIO.setup(R3, GPIO.OUT)
    GPIO.setup(R4, GPIO.OUT)

    # Make sure to configure the input pins to use the internal pull-down resistors

    GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # The readLine function implements the procedure discussed in the article
    # It sends out a single pulse to one of the rows of the keypad
    # and then checks each column for changes
    # If it detects a change, the user pressed the button that connects the given line
    # to the detected column

    def readLine(line, characters):
        GPIO.output(line, GPIO.HIGH)
        if (GPIO.input(C1) == 1):
            print(characters[0] + "\n")
        if (GPIO.input(C2) == 1):
            print(characters[1] + "\n")
        if (GPIO.input(C3) == 1):
            print(characters[2] + "\n")
        if (GPIO.input(C4) == 1):
            print(characters[3] + "\n")
        GPIO.output(line, GPIO.LOW)

    try:
        while True:
            # call the readLine function for each row of the keypad
            readLine(R1, ["1", "2", "3", "A"])
            readLine(R2, ["4", "5", "6", "B"])
            readLine(R3, ["7", "8", "9", "C"])
            readLine(R4, ["*", "0", "#", "D"])
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nApplication stopped!")