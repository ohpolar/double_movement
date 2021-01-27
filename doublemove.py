import keyboard, pyxinput

print("The script has started without error.")

def move_left(simCon):
    # Moves joystick to the Left
    simCon.set_value('AxisLx', -1)

def move_right(simCon):
    # Moves joystick to the Right
    simCon.set_value('AxisLx', 1)

def resetStick(simCon):
    # Keeps joystick at the center position for no micro movements in other directions.
    simCon.set_value('AxisLx', 0)

def main():
    simCon = pyxinput.vController(1)
    # infinite loop that detects for ('w+a') or ('w+d') in order to apply double movement
    while True:

        if keyboard.is_pressed('w+a'):
            move_left(simCon)
        
        elif keyboard.is_pressed('w+d'):
            move_right(simCon)

        else:
            resetStick(simCon)



main()