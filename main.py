#1. Setup connect on boot
#2. Setup pause/play
#3. Setup long hold = discoverable

import asyncio
from time import time, sleep
from gpiozero import LED, Button

led = LED(27)
button = Button(4)
discoverable = True

def setup_button_listener():
  print("setting up button listener")
  button.wait_for_press()
  t0 = time()
  print("you pressed the button")
  button.wait_for_release()
  t1= time()
  print("you released the button")
  hold_time = t1 - t0
  if hold_time > 2:
    led.on()
    print("alright, let's discover devices")
  else:

    if button.wait_for_press(timeout=0.6):
      print("fast forward")
    else:
      print("play/pause")



def main():
  print("starting up...")
  setup_button_listener()



main()
