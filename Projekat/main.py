import components.dht as dht
import settings as stg


def func_door_sensor():
    print("1")

def func_door_light():
    print("2")

def func_door_ultrasonic_sensor():
    print("3")

def func_door_buzzer():
    print("4")

def func_door_motion_sensor():
    print("5")

def func_door_membrane_switch():
    print("6")

def func_room_pir():
    print("7")

def func_room_dht():
    settings = stg.load_settings()
    dht.run_rdht1(settings)

def main():
    odgovor = 1
    while odgovor > 0:
        print("Odaberite opciju:\n")
        print("1) Door Sensor")
        print("2) Door Light")
        print("3) Door Ultrasonic Sensor")
        print("4) Door Buzzer")
        print("5) Door Motion Sensor")
        print("6) Door Membrane Switch")
        print("7) Room PIR")
        print("8) Room DHT")
        print("0) Kraj\n")
        odgovor = int(input())

        if(odgovor == 1):
            func_door_sensor()
        if(odgovor == 2):
            func_door_light()
        if(odgovor == 3):
            func_door_ultrasonic_sensor()
        if(odgovor == 4):
            func_door_buzzer()
        if(odgovor == 5):
            func_door_motion_sensor()
        if(odgovor == 6):
            func_door_membrane_switch()
        if(odgovor == 7):
            func_room_pir()
        if(odgovor == 8):
            func_room_dht()

if __name__ == '__main__':
    main()