import time


def run_door_buzzer(settings):
    settings = settings["DB"]
    if settings["simulated"]:
        print("Buzz!")
        time.sleep(1)

    else:
        from actuators.buzzer import buzzer_buzz
        buzzer_buzz(settings["pin"], 1)
