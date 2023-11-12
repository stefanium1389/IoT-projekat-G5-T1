import components.dht as dht
import components.led as led
import components.buzzer as buzzer
import components.ultrasound as ultrasound
import components.ds1 as ds1
import components.dpir1 as dpir1
import components.rpir1 as rpir1
import components.rpir2 as rpir2
import settings as stg


def func_door_sensor():
    ds1.run_ds1()

def func_door_light():
    settings = stg.load_settings()
    led.run_door_led(settings)

def func_door_ultrasonic_sensor():
    settings = stg.load_settings()
    ultrasound.run_door_ultrasound(settings)


def func_door_buzzer():
    settings = stg.load_settings()
    buzzer.run_door_buzzer(settings)

def func_door_motion_sensor():
    dpir1.run_dpir1()

def func_door_membrane_switch():
    print("6")

def func_room_pir():
    rpir1.run_rpir1()
    rpir2.run_rpir2()

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