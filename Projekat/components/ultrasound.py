from simulators.ultrasound import run_ultrasound_simulation
import time

def run_door_ultrasound(settings):
    settings = settings["DUS1"]
    if settings["simulated"]:
        print("Door ultrasound")
        d = run_ultrasound_simulation()
        print(f"Distance: {d} cm")
    else:
        from sensors.ultrasound import get_distance
        print("Door ultrasound")
        distance = get_distance()
        if distance is not None:
            print(f'Distance: {distance} cm')
        else:
            print('Measurement timed out')
        time.sleep(1)

