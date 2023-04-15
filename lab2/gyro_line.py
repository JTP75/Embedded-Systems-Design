from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


def frame_list(hand_color=(0,0,0),back_color=(128,128,128)):

    o = back_color
    x = hand_color

    frames = [

        [x,x,x,x,x,x,x,x,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
         x,x,x,x,x,x,x,x,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         x,x,x,x,x,x,x,x,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         x,x,x,x,x,x,x,x,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         x,x,x,x,x,x,x,x,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         x,x,x,x,x,x,x,x,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         x,x,x,x,x,x,x,x,
         o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         o,o,o,o,o,o,o,o,
         x,x,x,x,x,x,x,x],

    ]

    return frames

frames = frame_list((128,0,0),(0,0,0))

try:
    
    idx_prev = 4
    while True:
        d = sense.get_accelerometer_raw()
        y = d["y"]
        idx = int(7/2 * (y+1))
        c=( int(100*abs(y-1)),
            int(100*abs(1-abs(y))),
            int(100*abs(y+1)))
        if idx != idx_prev:
            sense.set_pixels(frame_list(c,(0,0,0))[idx])
            sleep(0.05)
        idx_prev = idx
        

except KeyboardInterrupt:
    print("\n\n=================================\nProgram Interrupted from terminal\n")