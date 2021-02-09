#!/usr/bin/env python3
from evdev import InputDevice
from select import select
import RPi.GPIO as GPIO
import time
from time import sleep
import subprocess
from subprocess import run
import datetime
import os
import sys
import re
import pygame
from pygame.locals import *
import pygame.display
import pygame.image
from pygame_functions import *
import random


def check_if_string_in_file(file_name, string_to_search):
    """Check if any line in the file contains given string"""
    with open(file_name,'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False




keys = "X^1234567890asdfghjklXXXXXycbnmXXXXXXXXXXXXXXXXXXXXXXX"
dev = InputDevice('/dev/input/event0')

pygame.init()
display = pygame.display.set_mode ((1024,600), pygame.NOFRAME)
img = pygame.image.load("/home/pi/WorkzDoor/Janitor.jpg")
pygame.mouse.set_cursor((8,8),(0,0), (0,0,0,0,0,0,0,0), (0,0,0,0,0,0,0,0))
display.blit(img, (0,0))
pygame.display.flip()


while True:
    #pygame.init()
    #display = pygame.display.set_mode ((1024,600), pygame.NOFRAME)
    #img = pygame.image.load("/home/pi/WorkzDoor/Janitor.jpg")
    #screenSize(0,0, pygame.NOFRAME)
    #wordBox = makeTextBox(10, 1, 1, 0, " ", 0, 10)
    #pygame.mouse.set_cursor((8,8),(0,0), (0,0,0,0,0,0,0,0), (0,0,0,0,0,0,0,0))
    #display.blit(img, (0,0))
    #pygame.display.flip()
    #pygame.event.clear()
    #entry = textBoxInput(wordBox)
    #input(entry)
    r,w,x = select([dev], [],[])
    for event in dev.read():
        if event.type==1 and event.value==1:
            if event.code==28:
                rfid_presented = ""
                e = rfid_presented
                if check_if_string_in_file("/home/pi/WorkzDoor/Loaded_Cards.txt", e):
                    videoPath = "/home/pi/WorkzDoor/ENTER.mp4"
                    omx = run(["omxplayer", '--win', '1,1,1024,600', videoPath])
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setwarnings(False)
                    GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
                    GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)
                    GPIO.output(26, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(26, GPIO.LOW)
                    GPIO.output(19, GPIO.HIGH)
                    time.sleep(5)
                    GPIO.output(19, GPIO.LOW)
                    count = 0
                    while count < 5:
                        GPIO.output(19, True)
                        time.sleep(0.3)
                        GPIO.output(19, False)
                        time.sleep(0.5)
                        count = count + 1
                    while count < 20:
                        GPIO.output(19, True)
                        time.sleep(0.05)
                        GPIO.output(19, False)
                        time.sleep(0.05)
                        count = count + 1

                else:
                    rfid_presented = ""

else:
    rfid_presented += keys[event.code]
del e

root.mainloop()