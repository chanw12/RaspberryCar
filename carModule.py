import RPi.GPIO as GPIO
from time import sleep, time


def default_settings():  # Must be called when you run car.
    # OTD = Leftmost, OTB = Leftless, OTA = Center, OTC = Rightless, OTE = Rightmost
    global MotorLeft_A, MotorLeft_B, MotorLeft_PWM, MotorRight_A, MotorRight_B, MotorRight_PWM, LeftPwm, RightPwm
    global trig, echo, OTD, OTB, OTA, OTC, OTE

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    # Motor pin settings
    MotorLeft_A = 12
    MotorLeft_B = 11
    MotorLeft_PWM = 35

    MotorRight_A = 15
    MotorRight_B = 13
    MotorRight_PWM = 37

    # Ultra sensor pin settings
    trig = 33
    echo = 31

    # Tracking sensor pin settings
    OTD = 16
    OTB = 18
    OTA = 22
    OTC = 40
    OTE = 32

    # Motor settings
    GPIO.setup(MotorLeft_A, GPIO.OUT)
    GPIO.setup(MotorLeft_B, GPIO.OUT)
    GPIO.setup(MotorLeft_PWM, GPIO.OUT)

    GPIO.setup(MotorRight_A, GPIO.OUT)
    GPIO.setup(MotorRight_B, GPIO.OUT)
    GPIO.setup(MotorRight_PWM, GPIO.OUT)

    # Ultra sensor settings
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    # Tracking sensor settings
    GPIO.setup(OTD, GPIO.IN)
    GPIO.setup(OTB, GPIO.IN)
    GPIO.setup(OTA, GPIO.IN)
    GPIO.setup(OTC, GPIO.IN)
    GPIO.setup(OTE, GPIO.IN)

    LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)
    RightPwm = GPIO.PWM(MotorRight_PWM, 100)

    LeftPwm.start(0)
    RightPwm.start(0)


def leftmotor(x):
    if x == True:
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
    elif x == False:
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    else:
        print('Config Error')


def rightmotor(x):
    if x == True:
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
    elif x == False:
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)

# ===================================
# forward0 = True, backward0 = False
# ===================================
# get go_any.py
# ===================================

def go_forward(speed, running_time):
    leftmotor(True)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    rightmotor(True)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)


def go_forward_diff(left_speed, right_speed):  # You can use this for curve turn.
    leftmotor(True)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    rightmotor(True)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(left_speed)
    RightPwm.ChangeDutyCycle(right_speed)


def go_forward_any(speed):
    leftmotor(True)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    rightmotor(True)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)


def stop():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)


def pwm_low():  # When occur KeyboardInterrupt
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()

# =============================
# get TurnModule.py
# =============================

def rightSwingTurn(speed, running_time):
    leftmotor(True)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
    GPIO.output(MotorRight_PWM,GPIO.LOW)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(0)
    sleep(running_time)


def leftSwingTurn(speed, running_time):
    rightmotor(True)
    GPIO.output(MotorLeft_PWM,GPIO.LOW)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)


def rightPointTurn(speed, running_time):
    leftmotor(True)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    rightmotor(False)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)


def leftPointTurn(speed, running_time):
    leftmotor(False)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    rightmotor(True)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)

# =============================
# get ultraModule.py
# =============================

def getDistance():
    GPIO.output(trig,False)
    sleep(0.1)
    GPIO.output(trig,True)
    sleep(0.00001)
    GPIO.output(trig,False)
    while GPIO.input(echo) == 0:
        pulse_start= time()
    while GPIO.input(echo) == 1:
        pulse_end = time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17000
    distance = round(distance,2)
    return distance


def get_DBACE():
    return [GPIO.input(OTD),
            GPIO.input(OTB),
            GPIO.input(OTA),
            GPIO.input(OTC),
            GPIO.input(OTE)]

if __name__ == '__main__':
    # Test Tracking Module
    try:
        default_settings()
        while True:
            print("leftmostled  detects black line(0) or white ground(1): " + str(GPIO.input(OTD)))
            print("leftlessled  detects black line(0) or white ground(1): " + str(GPIO.input(OTB)))
            print("centerled    detects black line(0) or white ground(1): " + str(GPIO.input(OTA)))
            print("rightlessled detects black line(0) or white ground(1): " + str(GPIO.input(OTC)))
            print("rightmostled detects black line(0) or white ground(1): " + str(GPIO.input(OTE)))
            sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()