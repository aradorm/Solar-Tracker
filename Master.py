import cv2
import numpy as np
import ephem
import RPi.GPIO as gpio
#import Controller
#import Motor
#import GUI

class Motor(object):
    def __init__(self, Type='Stepper', HomeAngle=0, MicroStep=1, EncodVal=1):
        self.Type=Type
        self.HomeAngle=HomeAngle
        self.MicroStep=MicroStep
        self.EncodVal
    def Drive(self):
        pass
    def Position(self):
        pass
    
class PIController(object):
    def __init__(self, Kp=1, Ki=1, dt=1, intg=0, err):
        self.Kp=Kp
        self.Ki=Ki
        self.dt=dt
        self.intg=intg
        self.err=err 
    def signal(self):
        signal=Kp*err+Ki*intg
        return signal
        intg=intg+err*dt
        
class sourse(object):
    

def main():
    #setup
   
    #loop
    
if __name__ == '__main__':
    main()
