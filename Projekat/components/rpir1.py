def run_rpir1(settings):
    settings = settings["RPIR1"]
    if settings["simulated"]:
        print("Motion detected! RPIR1\n")

    else:
        from sensors.pir import pir_scan
        pir_scan(settings["pin"], "RPIR1")
