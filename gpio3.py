
# import libraries
import gpiozero as gz
import os
import time

# create led objects
red = gz.LED(18)
blue = gz.LED(23)
green = gz.LED(24)

# def blink function
def blink(led, led_color, user_interval, user_blinks):
    print("You chose the", led_color, "LED.")
    for blink in user_blinks:
        led.on()
        time.sleep(user_interval)
        led.off()
        time.sleep(user_interval)

# program loop
led_again = "Y"
while led_again == "Y" or led_again == "y":

    # clear screen and print menu
    os.system("clear")

    print("""
    Which LED do you want to blink?

    1. Red
    2. Blue
    3. Green
    """)

    # user inputs
    choice = int(input("Enter the LED to blink (1, 2, or 3): "))
    interval = int(input("Enter the number of seconds to keep the LED lit: "))
    blinks = int(input("Enter the number of times to blink the light: "))

    # blink correct led
    if choice == 1:
        blink(red, "red", interval, blinks)
    elif choice == 2:
        blink(blue, "blue", interval, blinks)
    elif choice == 3:
        blink(green, "green", interval, blinks)
    else:
        print("That is not a valid choice.")

    led_again = input("Do you want to blink another LED (Y or N)? ")