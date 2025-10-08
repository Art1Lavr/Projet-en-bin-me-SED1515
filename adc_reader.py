
# lit une valeur analogique (ADC) à partir d’un
# potentiomètre connecté au GPIO26 et l’envoie au second Pico

from machine import ADC, Pin, UART
from time import sleep

# Le potentiomètre est connecté au GPIO26.
adc = ADC(Pin(26))

# UART0 : TX sur GPIO0, RX sur GPIO1, à 9600 bauds.
uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))

# main Boucle
while True:
    valeur = adc.read_u16()  # Lecture de la valeur ADC (0 à 65535)
    uart.write(str(valeur) + "\n")  # Envoi de la valeur au Pico 2
    print("Valeur envoyée :", valeur)  # Affichage pour le test
    sleep(0.1)  # Petite pause pour ne pas envois  trop rapide beacoup le signale
