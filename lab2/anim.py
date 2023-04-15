from sense_hat import SenseHat
import datetime as dt
import lib

sense = SenseHat()


def clk_frames(hand_color=(0,0,0),back_color=(128,128,128)):

    o = back_color
    x = hand_color

    frames = [

        [o,o,o,o,x,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,x,o,
        o,o,o,o,o,x,o,o,
        o,o,o,o,o,x,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,x,
        o,o,o,o,o,o,x,o,
        o,o,o,o,o,x,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,x,x,x,x,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,o,x,x,o,
        o,o,o,o,o,o,o,x,
        o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,o,x,o,o,
        o,o,o,o,o,x,o,o,
        o,o,o,o,o,o,x,o],

        [o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,x,o,o,o],

        [o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,x,o,o,o,o,
        o,o,o,x,o,o,o,o,
        o,o,x,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,x,x,o,o,o,o,
        x,x,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        x,x,x,x,x,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        x,x,o,o,o,o,o,o,
        o,o,x,x,o,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o],

        [o,o,x,o,o,o,o,o,
        o,o,x,o,o,o,o,o,
        o,o,o,x,o,o,o,o,
        o,o,o,x,o,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o],

    ]

    return frames

frames = clk_frames()

try:
    i_prev = 0
    while True:
        datetime = dt.datetime.now()
        t = datetime.time().second
        i = int(t%12)
        if i != i_prev:
            sense.set_pixels(frames[i])
        i_prev = i


except KeyboardInterrupt:
    print("\n\n=================================\nProgram Interrupted from terminal\n")