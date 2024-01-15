import sensor, image, time, lcd
from modules import ybserial, ybrgb
from fpioa_manager import fm
from machine import Timer,PWM
import _thread
from TBN.ver1.1beta import learing_color as lc


def SelfTest(mod=1):
    RGB = ybrgb()

    BEEP_PIN = 17
    fm.register(BEEP_PIN, fm.fpioa.GPIOHS0, force=True)

    tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
    ch = PWM(tim, freq=1000, duty=50, pin=BEEP_PIN)
    ch.duty(0)
    if mod == 1:
        for i in range(10):
            ch.duty(i+10)
            print("This is"+str(i))
            time.sleep(2)

        ch.duty(0)
        print("Beep tests ok")
    elif mod == 0:
        print()
        pass
    else:
        print("Nothing to do.This function self-destroy in 1 s.")
        time.sleep(1)



print("This file is for main process.Pls run the main process.")
color = lc()
time.sleep(0.3)
SelfTest(mod=int(input("mod?")))
print("Done\nEntering Main.py")
print(fps)