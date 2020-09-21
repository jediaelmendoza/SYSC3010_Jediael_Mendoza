from sense_hat import SenseHat
import time

sense = SenseHat()
sense.low_light = True

red = (255, 0, 0)
blue = (0, 0, 255)
nothing = (0, 0, 0)

def update_screen(mode):
    if mode == "first":
        sense.show_letter("J", blue, nothing)

    elif mode == "second":
        sense.show_letter("M", red, nothing)

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