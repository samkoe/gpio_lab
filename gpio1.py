# from gpiozero import LED 
# from time import sleep

import gpiozero
import time

red = gpiozero.LED(18)

while True: 
    red.on()
    time.sleep(1)
    red.off()
    time.sleep(1)