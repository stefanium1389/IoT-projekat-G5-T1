def run_dms(settings):
    settings = settings["DMS"]
    if settings["simulated"]:
        print("Membrane switch activated! DMS\n")

    else:
        from sensors.membrane_switch import membrane_switch_scan
        membrane_switch_scan(settings["pins"])