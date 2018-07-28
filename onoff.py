import RPi.GPIO as GPIO

SwitchPin = 2
PowerLEDPin = 3  

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SwitchPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(PowerLEDPin, GPIO.IN)

def on():
    return None

def off():
    return None

def detect():
    PC = off
    return PC
