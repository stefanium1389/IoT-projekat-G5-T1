def run_ds1(settings):
    settings = settings["DS1"]
    if settings["simulated"]:
        print("Button pressed! DS1")

    else:
        from sensors.button import button_scan
        button_scan(settings["pin"], "DS1")