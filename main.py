#1. Setup connect on boot

#2. Setup pause/play

#3. Setup long hold = discoverable


from gpiozero import PWMLED

led = PWMLED(27)

class Main:
  def __init__(self):
    print("hello there we are initializing")
    discoverable = True
    while discoverable:
      self.throbbing_led()


  def throbbing_led(self):
    led.on()

Main()
