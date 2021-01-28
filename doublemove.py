import keyboard, pyxinput

print("The script has started without error.")

def move_forward(simCon):
    # Moves joystick forwards
    simCon.set_value('AxisLy', 1)

def move_backward(simCon):
    #moves joystick backwards
    simCon.set_value('AxisLy', -1)

def move_left(simCon):
    # Moves joystick to the Left
    simCon.set_value('AxisLx', -32768)
    simCon.set_value('AxisLy', -8150)

def move_right(simCon):
    # Moves joystick to the Right
    simCon.set_value('AxisLx', 1)
    simCon.set_value('AxisLy', -8150)

def move_backLeft(simCon):
    # moves joystick back and to the left
    simCon.set_Value('AxisLx', 8000)
    simCon.set_Value('AxisLy', -1)

def move_backRight(simCon):
    # moves joystick back and to the right
    simCon.set_Value('AxisLx', 8000)
    simCon.set_Value('AxisLy', -1)

def resetStick(simCon):
    # Keeps joystick at the center position for no micro movements in other directions.
    simCon.set_value('AxisLx', 0)
    simCon.set_value('AxisLy', 0)

def resetStickSides(simCon):
    # resets the sticks x coordinates to 0 when walking forwards or backwards
    simCon.set_value('AxisLx', 0)

def main():
    simCon = pyxinput.vController(1)
    # infinite loop that detects for ('w+a') or ('w+d') in order to apply double movement
    while True:

        if keyboard.is_pressed('w+a'):
            move_left(simCon)
        
        elif keyboard.is_pressed('w+d'):
            move_right(simCon)
        
        elif keyboard.is_pressed('w'):
            move_forward(simCon)
            resetStickSides(simCon)
        
        elif keyboard.is_pressed('s'):
            move_backward(simCon)
            resetStickSides(simCon)
        
        elif keyboard.is_pressed('s+a'):
            move_backLeft(simCon)
        
        elif keyboard.is_pressed('s+d'):
            move_backRight(simCon)
        
        else:
            resetStick(simCon)



main()