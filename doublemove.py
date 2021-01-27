import sys, subprocess

# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'pyvjoy'])
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'keyboard'])


import pyvjoy, keyboard
# import joystick


print("The script has started without error.")


def move_left(vjoy):
    #print("This will move the joystick to the left.")
    vjoy.set_axis(pyvjoy.HID_USAGE_X, 0x0)


def move_right(vjoy):
    #print("this will move the joystick to the right.")
    vjoy.set_axis(pyvjoy.HID_USAGE_X, 0x8000)

def resetStick(vjoy):
    #print("The joystick has returned to the neutral position")
    vjoy.set_axis(pyvjoy.HID_USAGE_X, 0x4000)

def main():
    device = pyvjoy.VJoyDevice(1)
    # infinite loop that detects for ('w+a') or ('w+d') in order to apply double movement
    while True:

        if keyboard.is_pressed('w+a'):
            move_left(device)
        
        elif keyboard.is_pressed('w+d'):
            move_right(device)

        else:
            resetStick(device)



main()