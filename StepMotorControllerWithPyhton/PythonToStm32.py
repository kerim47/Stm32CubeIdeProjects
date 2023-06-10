from asyncio import sleep
import serial
import time

# port değerlerinin taninlanmasi

port = serial.Serial(
    port='COM5',
    baudrate=9600
)

def ileri():
    port.write(b'w') # aci derecesi
def geri():
    port.write(b's') # aci derecesi
def sag():
    port.write(b'a') # sola dondurur
def sol():
    port.write(b'd') # sağa dondurur

try:
    port.close()
    port.open()
    print("Bağlantı başarılı")
    while True:
        data = input() # girilen değere göre yon ve aci degerlerinin belirlenmesi
        port.write(data.encode()) # Degerin port' a yazdirilmasi
        s = port.read()           # Porttan gelen verilerin okunmasi
        # Verilerin ekrana yazdirilmasi
        print(data.encode())
        print(s.decode())
except:
    print("bağlantı hatası")
