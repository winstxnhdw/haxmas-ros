from gpiozero import LED
from time import * 

red = LED(22) 
yellow = LED(27) 
green = LED(17) 
duration = 0 
delay = 0.1 

def Red(duration): 

    start = time() 
    stop = time() + duration 

    while (time()<stop): 
        red.on() 
        sleep(delay) 
        red.off() 
        sleep(delay) 
        
def Yellow(duration): 

    start = time() 
    stop = time() + duration 
    
    while (time()<stop): 
        yellow.on() 
        sleep(delay) 
        yellow.off() 
        sleep(delay) 
        
def Green(duration): 

    start = time() 
    stop = time() + duration 
    
    while (time()<stop): 
        green.on() 
        sleep(delay) 
        green.off() 
        sleep(delay) 
        
def Mix(duration): 
    
    start = time() 
    stop = time() + duration 
    
    while (time()<stop): 
        green.on() 
        red.on() 
        sleep(delay) 
        yellow.on() 
        green.off() 
        sleep(delay) 
        red.off() 
        green.on() 
        yellow.on() 
        sleep(delay) 
        green.off() 
        red.on() 
        yellow.off() 
        sleep(delay) 
        
def Clear(): 
    
    red.off() 
    yellow.off() 
    green.off() 
    
    while 1: 
        Yellow(1) 
        Green(1) 
        Red(1) 
        Mix(5) 
        Clear()

def flash_red():
    pass

def flash_orange():
    pass

def flash_green():
    pass

def flash_all():
    pass