from machine import Pin, UART
import time

# Configuration du UART
uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))  # UART1 (TX=GP8, RX=GP9)
# Initialisation du buffer pour stocker les donnees recrues
buffer = b""
# Boucle principale
while True:
    if uart.any():
        data = uart.read(1)  
        if data == b"\n":
            try:
                value = int(buffer.decode().strip())
                print("Received value:", value)
            except:
                print("Invalid data:", buffer)
            buffer = b""
        else:
            buffer += data
# Petite pause pour eviter de surcharger le CPU
    time.sleep(0.01)
