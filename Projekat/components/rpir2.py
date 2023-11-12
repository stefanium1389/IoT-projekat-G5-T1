def run_rpir2(settings):
    settings = settings["RPIR2"]
    if settings["simulated"]:
        print("Motion detected! RPIR2\n")

    else:
        from sensors.pir import pir_scan
        pir_scan(settings["pin"], "RPIR2")
