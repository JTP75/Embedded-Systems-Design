from sense_hat import SenseHat
from time import sleep
import numpy as np

sense = SenseHat()

try:
    def diag(dg):
        sense.clear()

        rgb = np.zeros((511,3),dtype=int)
        tfs = np.arange(256,dtype=int)
        rgb[:256,0] = tfs[::-1]
        rgb[:256,1] = tfs
        rgb[255:,1] = tfs[::-1]
        rgb[255:,2] = tfs


        if dg<8:
            row = dg
            for i in range(row+1):
                c = tuple(rgb[int((i+0.01)/(row+0.1)*510)])
                sense.set_pixel(row-i, i, c)
        else:
            col = 14-dg
            for j in range(col+1):
                c = tuple(rgb[int((j+0.01)/(col+0.1)*510)])
                sense.set_pixel(7-j, 7-(col-j), c)
                '''
                255 0 0
                254 1 0
                ...
                1 254 0
                0 255 0
                0 254 1
                ...
                0 1 254
                0 0 255
                '''

    i=0
    #diag_prev
    while True:
        diag(i)
        i += 1
        i %= 15
        sleep(0.5)

except KeyboardInterrupt:
    sense.clear()
    print("\n\n=================================\nProgram Interrupted from terminal\n")