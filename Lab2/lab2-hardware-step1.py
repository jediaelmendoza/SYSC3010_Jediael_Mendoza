from sense_hat import SenseHat
import time

sense = SenseHat()
sense.low_light = True

red = (255, 0, 0)
blue = (0, 0, 255)
nothing = (0, 0, 0)

def first_initial():
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, B, B, O, O,
    O, O, O, O, B, B, O, O,
    O, O, O, O, B, B, O, O,
    O, B, B, O, B, B, O, O,
    O, B, B, O, B, B, O, O,
    O, B, B, O, B, B, O, O,
    O, O, B, B, B, O, O, O,
    ]
    return logo 

def sec_initial():
    R = red
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    R, R, O, O, O, R, R, O,
    R, R, R, O, R, R, R, O,
    R, R, O, R, O, R, R, O,
    R, R, O, R, O, R, R, O,
    R, R, O, O, O, R, R, O,
    R, R, O, O, O, R, R, O,
    R, R, O, O, O, R, R, O,
    ]
    return logo

def update_screen(mode):
    if mode == "first":
        sense.set_pixels(first_initial())

    elif mode == "second":
       sense.set_pixels(sec_initial())

#Start
update_screen("first");
cur = "first"
while True:
    selection = False
    events = sense.stick.get_events()
    for event in events:
        if event.action != "released":
            if event.direction == "left" or "right" or "up" or "down":
                selection = True
            if selection:
                if cur == "first":
                    update_screen("second")
                    cur = "second"
                else:
                    update_screen("first")
                    cur = "first"