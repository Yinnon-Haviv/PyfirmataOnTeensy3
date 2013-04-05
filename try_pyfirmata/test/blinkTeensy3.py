'''
Created on Apr 5, 2013

@author: yinnonhaviv
'''

from test import Teensy3

def main():
    # Simple blink example using the onboard led.
    board = Teensy3.Teensy3('/dev/cu.usbmodem12341')
    led_pin = board.get_pin('d:13:o')
    while(True):
        led_pin.write(1)
        board.pass_time(0.5)
        led_pin.write(0)
        board.pass_time(0.5)

if __name__ == '__main__':
    main()