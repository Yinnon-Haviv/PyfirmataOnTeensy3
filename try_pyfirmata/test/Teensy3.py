'''
Created on Apr 5, 2013

@author: yinnonhaviv
'''

from pyfirmata import Board

class Teensy3(Board):
    """
    A board that wil set itself up as a Teensy 3.0.
    """
    layout = {
        'digital' : tuple(x for x in range(34)),
        'analog' : tuple(x for x in range(14, 24) + range(34, 38)),
        'pwm' : tuple(x for x in range(34)),
        'use_ports' : True,
        'disabled' : (0, 1) # Rx, Tx, Crystal. TODO:is that necessary?
    }
    def __init__(self, *args, **kwargs):
        args = list(args)
        args.append(Teensy3.layout)
        super(Teensy3, self).__init__(*args, **kwargs)
        
    def __str__(self):
        return 'Teensy3 %s on %s' % (self.name, self.sp.port)
 
 
