import FuncFile as fun
def main():
    Android = fun.Consts
    represent = fun.NmeaRepr
    parameters = Android(adb_ip="127.0.0.1", adb_port=5037)
    parameters.connect()
    nmea_repr = represent()
    lat, lon, alt, bear = parameters.get_floats()
    output1, output2 = nmea_repr.represent(lat, lon, alt, bear)
    print(output1, output2)

if __name__ == "__main__":
    main()