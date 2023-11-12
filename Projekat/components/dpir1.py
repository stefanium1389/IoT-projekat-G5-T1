def run_dpir1(settings):
    settings = settings["DPIR1"]
    if settings["simulated"]:
        print("Motion detected! DPIR1\n")

    else:
        from sensors.pir import pir_scan
        pir_scan(settings["pin"], "DPIR1")
