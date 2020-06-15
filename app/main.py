from time import sleep
from gpiozero import LED

LED_PIN = 17

led = LED(LED_PIN)

i = 0
while True:
    print(f'{i} - Blink!')
    led.on()
    sleep(1)
    led.off()
    sleep(5)
    i += 1
