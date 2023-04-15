# Embedded-Systems-Design
University of Pittsburgh ECE 1175

## Brief
Embedded programming on Raspberry Pi using C/C++/Python/Bash. The course covered design methodology, peripheral interfacing, and operating systems.

## Semester
Spring 2023

# Labs
## Lab 1 - Introduction
The task for the first lab was to demonstrate the functionality of the Raspberry Pi. To do so, I attached the board to a chassis with two FS90R continuous servos and a wheel for each servo (See lab1_rover.png). I later added a USB webcam to record video. On the software side, I used the python packages pygame, cam, and gpiozero to implement a real-time W-A-S-D control scheme. To reduce servo jittering, I experimented with different gpio factories and settled on the PiGPIOFactory.
## Lab 2 - Sense Hat
Lab 2 focused on utilizing the sensors and actuators of the Raspberry Pi Sense Hat attachment. Animations were done using a 8x8 LED array.
* Analog clock animation (anim.py)
* Color-changing diagonal animation (diagonal.py)
* An animated line that reacts to gyroscopic changes (gyro_line.py)
* An animation that responds to joystick inputs (joystick.py)
* A repeating timer written in C (timer.c)
## Lab 3 - GPIO and CPU Cache
For the third lab, I wrote two C++ programs to blink the r/w integrated LED. The first (blink_VFM.cpp) modifies the trigger and blinks the LED using the linux virtual file system. The other one (blink_devmem.cpp) uses the virual memory (/dev/mem) and memory mapping functions to accomplish the same task. In addition, we wrote a code to perform matrix multiplication while optimizing CPU cache usage. We use 'perf' to measure the cache miss rate at runtime.
