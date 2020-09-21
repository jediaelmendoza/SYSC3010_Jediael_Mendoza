from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
while True:
    #Coordinates
    x = randint(0,7)
    y = randint(0,7)

    #RGB
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    
    #Start
    sense.set_pixel(x,y,r,g,b)
    sleep(0.25)