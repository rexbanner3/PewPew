# import time
import gpiozero
# import RPi.GPIO as gpio
import time
import signal
import pygame 

trig_pin = "GPIO26"

trig = gpiozero.Button(trig_pin, pull_up=False)
pygame.init()

# pygame.mixer.music.load("/home/keck5/PyProjects/PewPew/Laser1.wav")
blaster = ("/home/keck5/PyProjects/PewPew/Blaster.wav")
chewey = "/home/keck5/PyProjects/PewPew/Sounds/chewy_roar.wav"
blaster2 = "/home/keck5/PyProjects/PewPew/Sounds/blaster-firing.wav"
iMarch = "/home/keck5/PyProjects/PewPew/Sounds/imperial_march.wav"
pygame.mixer.music.load(blaster2)
def output():
    pygame.mixer.music.play()
    # pygame.event.wait()
trig.when_pressed = output

signal.pause()

