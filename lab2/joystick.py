from sense_hat import SenseHat

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

        [o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o],

        [o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,x,o,x,o,o,
        o,o,o,o,x,o,o,o,
        o,o,o,x,o,x,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o],

    ]

    return frames

frames = clk_frames()

try:
    f = frames[12]
    f_prev = frames[12]
    while True:
        for event in sense.stick.get_events():
            if event.action == "pressed" or event.action == "held":
                print(event.action+"\t"+event.direction)
                if event.direction == "middle":
                    f = frames[13]
                elif event.direction == "up":
                    f = frames[0]
                elif event.direction == "down":
                    f = frames[6]
                elif event.direction == "left":
                    f = frames[9]
                elif event.direction == "right":
                    f = frames[3]
            else:
                f = frames[12]
                print(event.action+"\t"+event.direction)

        if f != f_prev:
            sense.set_pixels(f)

        f_prev = f
        





except KeyboardInterrupt:
    print("\n\n=================================\nProgram Interrupted from terminal\n")


    