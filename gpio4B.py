# gpio4B.py

# import libraries
import gpiozero as gz
import time
import os

# setup led and button object

red = gz.LED(18)
button = gz.Button(25)

# listen for button press
while True:
    if button.is_pressed:
        red.on()
        time.sleep(1)
        red.off()
    else:
        os.system("clear")      # clear the screen to make prompt clear
        print("Waiting for you to press the button...")
    time.sleep(.5)
