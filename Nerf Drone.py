import RPi.GPIO as GPIO
import time

import PiMotor

GPIO.setwarnings(False)

TRIG = 29
ECHO = 31

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

m1 = PiMotor.Motor("MOTOR1", 1)
m2 = PiMotor.Motor("MOTOR2", 1)

motorAll = PiMotor.LinkedMotors(m1, m2)


def stop():
    print("Robot Stop ")
    motorAll.stop()
    time.sleep(2)


def forward():
    print("Robot Moving Forward ")
    m1.forward(100)
    time.sleep(2)


def back():
    print("Robot Moving Backward ")
    m1.reverse(100)
    time.sleep(2)


def left():
    print("Robot Moving Left ")
    m1.stop()
    m2.stop()
    time.sleep(2)


def right():
    print("Robot Moving Right ")
    m1.forward(100)
    m2.forward(100)
    time.sleep(2)


stop()
count = 0
avgDistance = 0
i = 0
while True:

    for i in range(5):
        GPIO.output(TRIG, False)
        time.sleep(0.1)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        pulse_duration = pulse_end - time.time()

        distance = (pulse_duration * 34300)/2
        distance = round(distance, 2)
        avgDistance = avgDistance + distance

        avgDistance = avgDistance/5
        print(avgDistance)

    if avgDistance < 20:
        count = count + 1
        stop()
        time.sleep(1)
        back()
        time.sleep(2)
        if count % 4 == 1:
            right()

        else:
            forward()
