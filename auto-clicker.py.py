import time
import threading
import random 
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

print("Welcome. This auto-clicker uses variance to click randomly within a certain specified time period.")
print("The variance is used in such a way that the time between clicks is set to a minimum and then randomly picked for a maximum within set parameters by the user.")

print("")
print("")

print("To start the autoclicker once you have set your parameters, click the '[' character.")
print("To stop, simply click the ']' character.")

print("")
print("")

c = float(input("How many seconds (minimum) in between clicks: "))

print("The way this program uses variance in your auto-clicking is by using a normal bell curve centered at 0.")
print("The variance number you input is the standard deviation from 0. \nInputting variables higher than recommended can lead to exponential increases in varied click times.")


print("For instance, if you used a variance of 7, the numbers range anywhere from 'your preferred clicking speed' to 'your preferred speed + 14 seconds'.")

print("")
print("")

b = float(input("Please state your random variance for the varied clicking. \nI would this at around 1.8 (Warning - Going above 2 can create long variations) unless you know how standard deviation works. At 1.8, \nyou get around a 1-2 second ramdonmized delay after your minimum click time.: "))
delay = c
button = Button.left
start_stop_key = KeyCode(char='[')
exit_key = KeyCode(char=']')



class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False
  
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep((self.delay) + abs(random.normalvariate(0,b)))
            time.sleep(1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
    
    input('Thank you! Press ENTER to exit.')
import sys
sys.exit()