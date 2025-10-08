from machine import Pin, PWM, UART
import time
# configurer le PWM
pwm = PWM(Pin(15))
pwm.freq(1000)  # fréquence de 1 kHz
pwm.duty_u16(0)  # initialiser avec un rapport cyclique de 0%
#configurer l'UART
uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
# fonction pour changer le duty cycle
def set_duty(percent):
    if percent < 0:
        percent = 0
    elif percent > 100:
        percent = 100
    duty = int(percent * 65535 / 100)
    pwm.duty_u16(duty)
    return duty
# Envoyer la valeur PWM actuelle via UART
def send_pwm_value(duty):
    message = "PWM Duty Cycle: {}%\n".format(int(duty * 100 / 65535))
    uart.write(message)
# boucle principale
while True:
    for percent in range(0, 101, 10):
        duty = set_duty(percent)
        send_pwm_value(duty)
        print("Set PWM to {}%".format(percent))
        time.sleep(1)