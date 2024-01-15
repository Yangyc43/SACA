import machine

boot_key = machine.Pin(36, machine.Pin.IN, machine.Pin.PULL_UP)

if boot_key.value() == 0:
    print("Boot键已按下")
else:
    print("Boot键未按下")
