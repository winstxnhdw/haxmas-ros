from gpiozero import LED
from time import * 

red = LED(22) 
yellow = LED(27) 
green = LED(17)

duration = 0 
delay = 0.1 

def flash_red(duration): 

    start = time() 
    stop = time() + duration 

    while (time() < stop): 
        red.on() 
        sleep(delay) 
        red.off() 
        sleep(delay) 
        
def flash_orange(duration): 

    start = time() 
    stop = time() + duration 
    
    while (time() < stop): 
        yellow.on() 
        sleep(delay) 
        yellow.off() 
        sleep(delay) 
        
def flash_green(duration): 

    start = time() 
    stop = time() + duration 
    
    while (time() < stop): 
        green.on() 
        sleep(delay) 
        green.off() 
        sleep(delay) 
        
def flash_all(duration): 
    
    start = time() 
    stop = time() + duration 
    
    while (time() < stop): 
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