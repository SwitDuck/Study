import FuncFile as fun
def main():
    Android = fun.Consts
    parameters = Android(adb_ip="127.0.0.1", adb_port=5037)
    parameters.connect()
    output1, output2 = fun.NmeaRepr.represent(parameters)
    print(output1, output2)

if __name__ == "__main__":
    main()