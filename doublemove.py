import pyvjoy, keyboard, pyxinput

print("The script has started without error.")

#pyxinput.test_virtual()

def move_left(vjoy, simCon):
    # print("This will move the joystick to the left.")
    vjoy.set_axis(pyvjoy.HID_USAGE_X, 0x1)
    simCon.set_value('AxisLx', 0)


def move_right(vjoy, simCon):
    # print("this will move the joystick to the right.")
    vjoy.set_axis(pyvjoy.HID_USAGE_X, 0x8000)
    simCon.set_value('AxisLx', 1)

def resetStick(vjoy, simCon):
    # print("The joystick has returned to the neutral position")
    vjoy.set_axis(pyvjoy.HID_USAGE_X, 0x4000)
    simCon.set_value('AxisLx', 0)

def main():
    device = pyvjoy.VJoyDevice(1)
    simCon = pyxinput.vController(1)
    # infinite loop that detects for ('w+a') or ('w+d') in order to apply double movement
    while True:

        if keyboard.is_pressed('w+a'):
            move_left(device, simCon)
        
        elif keyboard.is_pressed('w+d'):
            move_right(device, simCon)

        else:
            resetStick(device, simCon)



main()