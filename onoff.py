#import RPi.GPIO as GPIO, 
import time

#change these variables to adjust which GPIO pin will be the SwitchPin for switching the PC on or off
SwitchPin = 2
#change these variables to adjust which GPIO pin will be the the PowerLED pin for detecting if the PC is on or not
PowerLEDPin = 3  


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(SwitchPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(PowerLEDPin, GPIO.IN)

def on():
    '''
    setup()
    time.sleep(0.5)
    GPIO.output(SwitchPin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.ouput(SwitchPin, GPIO.LOW)
    GPIO.cleanup()
    '''
    return "on"

def off():
    '''
    setup()
    time.sleep(0.5)
    GPIO.output(SwitchPin, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(SwitchPin, GPIO.LOW)
    GPIO.cleanup()
    '''

    return "off"

def detect():
    '''setup()
    test = GPIO.read(PowerLEDPin)
    '''
    test = True
    if test == True:
        PC = "on"
    elif test == False:
        PC = "off"
    else:
        PC = "WTF"
    return PC

#Uncomment the line below to switch the PC on
#on()

#Uncomment the line below to switch the PC off
#off()

#Uncomment the line below to detect if the PC is on or off
#print(detect())