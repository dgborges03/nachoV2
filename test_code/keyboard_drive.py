# Imports
from gpiozero import PWMOutputDevice
import curses
import time

# Define the motor pins.
BASE_SPEED = 155

# back right motor
PIN_BR_LEGA = 17
PIN_BR_LEGB = 27

# back left motor
PIN_BL_LEGA = 22
PIN_BL_LEGB = 23

# front left motor
PIN_FL_LEGA = 24
PIN_FL_LEGB = 25

# front right motor
PIN_FR_LEGA = 5
PIN_FR_LEGB = 6

# Constants to change speeds!
TRIM_FL = 1.0
TRIM_FR = 0.9
TRIM_BL = 1.0
TRIM_BR = 0.9


class Motor():
    """
    Motor object has 2 properties. Leg 1 and Leg 2. Drive the motor by
    creating a voltage difference between the two legs.
    """

    def __init__(self, lega, legb):
        self.LEG_a = PWMOutputDevice(lega, frequency=1000)
        self.LEG_b = PWMOutputDevice(legb, frequency=1000)

    def drive(self, speed, direction):
        value = speed / 255
        if direction:
            self.LEG_a.value = value
            self.LEG_b.value = 0
        else:
            self.LEG_b.value = value
            self.LEG_a.value = 0


def stop(motors):
    for m in motors:
        m.drive(0, True)


def driveForward(motorFL, motorFR, motorBL, motorBR):
    motorFL.drive(int(BASE_SPEED * TRIM_FL), True)
    motorFR.drive(int(BASE_SPEED * TRIM_FR), True)
    motorBL.drive(int(BASE_SPEED * TRIM_BL), True)
    motorBR.drive(int(BASE_SPEED * TRIM_BR), True)


def driveBackward(motorFL, motorFR, motorBL, motorBR):
    motorFL.drive(int(BASE_SPEED * TRIM_FL), False)
    motorFR.drive(int(BASE_SPEED * TRIM_FR), False)
    motorBL.drive(int(BASE_SPEED * TRIM_BL), False)
    motorBR.drive(int(BASE_SPEED * TRIM_BR), False)


def strafeLeft(motorFL, motorFR, motorBL, motorBR):
    motorFL.drive(BASE_SPEED, False)
    motorFR.drive(BASE_SPEED, True)
    motorBL.drive(BASE_SPEED, True)
    motorBR.drive(BASE_SPEED, False)


def strafeRight(motorFL, motorFR, motorBL, motorBR):
    motorFL.drive(BASE_SPEED, True)
    motorFR.drive(BASE_SPEED, False)
    motorBL.drive(BASE_SPEED, False)
    motorBR.drive(BASE_SPEED, True)


def rotateLeft(motorFL, motorFR, motorBL, motorBR):
    motorFL.drive(BASE_SPEED, False)
    motorFR.drive(BASE_SPEED, True)
    motorBL.drive(BASE_SPEED, False)
    motorBR.drive(BASE_SPEED, True)


def rotateRight(motorFL, motorFR, motorBL, motorBR):
    motorFL.drive(BASE_SPEED, True)
    motorFR.drive(BASE_SPEED, False)
    motorBL.drive(BASE_SPEED, True)
    motorBR.drive(BASE_SPEED, False)


def main(stdscr):
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    stdscr.timeout(150)

    motorBR = Motor(PIN_BR_LEGA, PIN_BR_LEGB)
    motorBL = Motor(PIN_BL_LEGB, PIN_BL_LEGA)
    motorFL = Motor(PIN_FL_LEGB, PIN_FL_LEGA)
    motorFR = Motor(PIN_FR_LEGA, PIN_FR_LEGB)

    motors = [motorFL, motorFR, motorBL, motorBR]

    stdscr.addstr(0, 0, "WASD to move, Left/Right arrows to rotate, Q to quit B-)")

    try:
        while True:
            key = stdscr.getch()

            if key == ord('w'):
                driveForward(motorFL, motorFR, motorBL, motorBR)
            elif key == ord('s'):
                driveBackward(motorFL, motorFR, motorBL, motorBR)
            elif key == ord('a'):
                strafeLeft(motorFL, motorFR, motorBL, motorBR)
            elif key == ord('d'):
                strafeRight(motorFL, motorFR, motorBL, motorBR)
            elif key == curses.KEY_LEFT:
                rotateLeft(motorFL, motorFR, motorBL, motorBR)
            elif key == curses.KEY_RIGHT:
                rotateRight(motorFL, motorFR, motorBL, motorBR)
            elif key == ord('q'):
                break
            else:
                stop(motors)

    finally:
        stop(motors)
        for m in motors:
            m.LEG_a.close()
            m.LEG_b.close()


if __name__ == "__main__":
    curses.wrapper(main)