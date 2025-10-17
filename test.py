from machine import Pin, PWM, UART
import time
# Configuración del pin PWM
pwm = PWM(Pin(19))
pwm.freq(1000)
pwm.duty_u16(0)
# configuración del UART
uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
# Initialisation du buffer pour stocker les donnees recrues
buffer = ""
# Boucle principale
while True:
    if uart.any():
        char = uart.read(1).decode() 
        if char == "\n":
            try:
                value = int(buffer.strip())
                percent = int(value / 65535 * 100)
                duty = int(percent * 65535 / 100)
                pwm.duty_u16(duty)
                print("Set PWM to {}%".format(percent))
            except:
                print("Errore en momemt de lire information:", buffer)
            buffer = ""  
        else:
            buffer += char
# Petite pause pour eviter de surcharger le CPU
    time.sleep(0.01)