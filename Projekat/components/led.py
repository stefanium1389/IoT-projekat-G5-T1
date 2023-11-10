import time


def run_door_led(settings):
    settings = settings["DL"]
    if settings["simulated"]:
        print("Door light on!")
        time.sleep(1)
        print("Door light off!")

    else:
        from actuators.dioda import run_led
        run_led(settings["pin"], 1)

