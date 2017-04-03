#!/usr/bin/env python

# Servo Control
import time
import wiringpi

PIN = 18
PWM_0 = 50
PWM_180 = 250

def swing():
    # use 'GPIO naming'
    wiringpi.wiringPiSetupGpio()

    # set #PIN to be a PWM output
    wiringpi.PINMode(PIN, wiringpi.GPIO.PWM_OUTPUT)

    # set the PWM mode to milliseconds stype
    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

    # divide down clock
    wiringpi.pwmSetClock(192)
    wiringpi.pwmSetRange(2000)

def swing():
    wiringpi.pwmWrite(PIN,PWM_0)
    time.sleep(2)
    wiringpi.pwmWrite(PIN,PWM_180)

