#!/usr/bin/env python

# Servo Control
import time
import wiringpi

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

pin = 18 

# set #pin to be a PWM output
wiringpi.pinMode(pin, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

#delay_period = 0.01 

wiringpi.pwmWrite(pin,50)

time.sleep(2)

wiringpi.pwmWrite(pin,250)

#while True:
#        for pulse in range(50, 250, 1):
#                wiringpi.pwmWrite(pin, pulse)
#                time.sleep(delay_period)
#        for pulse in range(250, 50, -1):
#                wiringpi.pwmWrite(pin, pulse)
#                time.sleep(delay_period)
