# gpio4.py

# import libraries
import gpiozero as gz
import time
import os

# setup button object

button = gz.Button(25)

# listen for button press
while True:
    if button.is_pressed:
        print("Button Pressed")
        time.sleep(1)
    else:
        os.system("clear")      # clear the screen to make prompt clear
        print("Waiting for you to press a button...")
    time.sleep(.5)
