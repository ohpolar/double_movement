import pyvjoy
a = pyvjoy.VJoyDevice(1)
print("The script has started without error.")


def move_left():
    #print("This will move the joystick to the left.")
    a.set_axis(pyvjoy.HID_USAGE_X, 0x0)


def move_right():
    #print("this will move the joystick to the right.")
    a.set_axis(pyvjoy.HID_USAGE_X, 0x8000)

def resetStick():
    #print("The joystick has returned to the neutral position")
    a.set_axis(pyvjoy.HID_USAGE_X, 0x4000)
