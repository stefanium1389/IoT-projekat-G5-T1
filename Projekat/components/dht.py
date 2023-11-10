from simulators.dht import run_dht_simulator
import threading
import time

def dht_callback(humidity, temperature, code):
    t = time.localtime()
    print("="*20)
    print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    print(f"Code: {code}")
    print(f"Humidity: {humidity}%")
    print(f"Temperature: {temperature}°C")


def run_rdht1(settings): #, threads, stop_event):
        settings = settings["RDHT1"]
        if settings['simulated']:
            #print("Starting rdht1 sumilator")
            run_dht_simulator(2, dht_callback)
            #dht1_thread = threading.Thread(target = run_dht_simulator, args=(2, dht_callback, stop_event))
            #dht1_thread.start()
            #threads.append(dht1_thread)
            #print("Dht1 sumilator started")
        else:
            from sensors.dht import run_dht_loop, DHT
            #print("Starting rdht1 loop")
            dht = DHT(settings['pin'])
            #dht1_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, dht_callback, stop_event))
            #dht1_thread.start()
            #threads.append(dht1_thread)
            #print("Dht1 loop started")
