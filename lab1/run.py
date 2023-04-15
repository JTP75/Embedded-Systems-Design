from os import system
from multiprocessing import Process
from cam.video_capture import VideoCaptureAsync
from cam.camera_record import record_video
system("sudo pigpiod") # start pigpio daemon

from gpiozero import Servo, Device
from gpiozero.pins.pigpio import PiGPIOFactory
import pygame

# wheel speed parameters
# (due to imperfections in the continuous servos)
Lstop = -0.0
Rstop = -0.1
Lspeed = 0.2
Rspeed = 0.2

record_time = 20

Device.pin_factory = PiGPIOFactory()

pygame.init()
# 12R & 13L
right = Servo(12)
left = Servo(13)
right.value=Rstop
left.value=Lstop

window = pygame.display.set_mode((640,480))
pygame.display.set_caption("PiCar")
cam_record = Process(target = record_video)
cam_record.start()


moop=True;
while moop:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            moop==False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left.value = Lstop + Lspeed
                right.value = Rstop - Rspeed
            elif event.key == pygame.K_a:
                left.value = Lstop - Lspeed
                right.value = Rstop - Rspeed
            elif event.key == pygame.K_s:
                left.value = Lstop - Lspeed
                right.value = Rstop + Rspeed
            elif event.key == pygame.K_d:
                left.value = Lstop + Lspeed
                right.value = Rstop + Rspeed
        else:
            left.value = Lstop
            right.value = Rstop
            
pygame.quit()

system("sudo killall pigpiod") # kill pigpio daemon