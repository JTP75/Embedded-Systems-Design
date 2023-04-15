# Embedded-Systems-Design
University of Pittsburgh ECE 1175

## Brief
Embedded programming on Raspberry Pi using C/C++/Python/Bash. The course covered design methodology, peripheral interfacing, and operating systems.

## Semester
Spring 2023

# Labs
## Lab 1
The task for the first lab was to demonstrate the functionality of the Raspberry Pi. To do so, I attached the board to a chassis with two FS90R continuous servos and a wheel for each servo (See lab1_rover.png). I later added a USB webcam to record video. On the software side, I used the python packages pygame, cam, and gpiozero to implement a real-time W-A-S-D control scheme. To reduce servo jittering, I experimented with different gpio factories and settled on the PiGPIOFactory.
