'''class server():
    import subprocess as sub
    import psutil
    def comma_input(): #Ввод консольной команды
        ip = input("Введите IP адрес")
        changer = input("Введите значение, какой тип подключения будет использоваться(1-Ethernet, 2-WiFi)")
        if changer == 1: 
            changer = 'ethernet'
            name_eth = input("Введите имя сети ethernet")
        else: 
            changer = 'wifi'
            name_wifi = input("Введите имя сети WiFi") 
        def last_eth():
            lid_eth = psutil.net_if_stats()
            dicteth = lid_eth.keys()
            return len(dicteth)+1
            ...
        def last_wifi():
            lid_wifi = psutil.net_if_stats()
            dictwifi = lid_wifi.keys()
            return len(dictwifi)+1
            ...
        znach1= last_eth()
        ip_adr = input('Введите ip адрес')
        mask = input('Введите маску в десятичном')
        gateway = input('ВВедите шлюз')
        sub.run(f'nmcli', 'connection', 'add', 'type', 'ethernet', 'ifname', 'eth{znach1}', 'con-name', 'name_eth', 'ipv4.method', 'manual ipv4.addresses', "{ip_adr}/{mask}", 'ipv4.gateway', "{gateway}")
        #nmcli connection add type ethernet ifname eth0 con-name MyEthernetConnection ipv4.routes "192.168.1.0/24 192.168.0.1" ipv4.method manual ipv4.addresses "192.168.0.100/24" ipv4.gateway "192.168.0.1"
        #nmcli connection add type wifi ifname wlan0 con-name MyWiFiConnection ssid "MySSID" ipv4.routes "192.168.2.0/24 192.168.1.1" ipv4.method manual ipv4.addresses "192.168.1.100/24" ipv4.gateway "192.168.1.1"
    comma_input()
    ...
'''
import subprocess as sub
import psutil

class Server:
    def comma_input(self):  # Ввод консольной команды
        changer = input("Введите значение, какой тип подключения будет использоваться (1-Ethernet, 2-WiFi): ")
        if changer == "1":
            changer = 'ethernet'
            name_eth = input("Введите имя сети Ethernet: ")
        else:
            changer = 'wifi'
            name_wifi = input("Введите имя сети WiFi: ")

        def last_eth():
            lid_eth = psutil.net_if_stats()
            dicteth = lid_eth.keys()
            return len(dicteth) + 1

        def last_wifi():
            lid_wifi = psutil.net_if_stats()
            dictwifi = lid_wifi.keys()
            return len(dictwifi) + 1

        znach1 = last_eth() if changer == 'ethernet' else last_wifi()
        ip_adr = input("Введите IP адрес: ")
        mask = input("Введите маску в десятичном виде: ")
        gateway = input("Введите шлюз: ")

        if changer == 'ethernet':
            sub.run([
                'nmcli', 'connection', 'add',
                'type', 'ethernet',
                'ifname', f'eth{znach1}',
                'con-name', name_eth,
                'ipv4.method', 'manual',
                'ipv4.addresses', f"{ip_adr}/{mask}",
                'ipv4.gateway', gateway
            ])
        else:
            sub.run([
                'nmcli', 'connection', 'add',
                'type', 'wifi',
                'ifname', f'wlan{znach1}',
                'con-name', name_wifi,
                'ipv4.method', 'manual',
                'ipv4.addresses', f"{ip_adr}/{mask}",
                'ipv4.gateway', gateway
            ])
server_instance = Server()
server_instance.comma_input()

class configmanager():
    ...
class tasksheduler():
    ...
class usermanager():
    ...