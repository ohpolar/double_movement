import keyboard, pyxinput

print("The script has started without error.")

def move_forward(simCon):
    # Moves joystick forwards
    simCon.set_value('AxisLy', 1)
    print("forward")

def move_backward(simCon):
    #moves joystick backwards
    simCon.set_value('AxisLy', -1)
    print("backward")

def move_true_left(simCon):
    simCon.set_value('AxisLx', -1)
    print("true_left")

def move_true_right(simCon):
    simCon.set_value('AxisLx', 1)
    print("true_right")

def move_left(simCon):
    # Moves joystick to the Left
    simCon.set_value('AxisLx', -32768)
    simCon.set_value('AxisLy', -10000) # using -8150 here will give you around max angle.
    print("diagonal left")

def move_right(simCon):
    # Moves joystick to the Right
    simCon.set_value('AxisLx', 1)
    simCon.set_value('AxisLy', -10000) # using -8150 here will give you around max angle.
    print("diagonal right")

def move_backLeft(simCon):
    # moves joystick back and to the left
    simCon.set_value('AxisLx', -32768)
    simCon.set_value('AxisLy', -1)
    print("backleft")

def move_backRight(simCon):
    # moves joystick back and to the right
    simCon.set_value('AxisLx', 1)
    simCon.set_value('AxisLy', -1)
    print("backright")

def resetStick(simCon):
    # Keeps joystick at the center position for no micro movements in other directions.
    simCon.set_value('AxisLx', 0)
    simCon.set_value('AxisLy', 0)

def reset_stick_x(simCon):
    # resets the sticks x coordinates to 0 when walking forwards or backwards
    simCon.set_value('AxisLx', 0)

def reset_stick_y(simCon):
    # resets the sticks y coordinates to 0 when walking true left or true right
    simCon.set_value('AxisLy', 0)

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
            reset_stick_x(simCon)

        elif keyboard.is_pressed('a'):
            move_true_left(simCon)
           # reset_stick_y(simCon)
        
        elif keyboard.is_pressed('d'):
            move_true_right(simCon)
            #reset_stick_y(simCon)

        elif keyboard.is_pressed('s'):
            move_backward(simCon)
            reset_stick_x(simCon)
        
        elif keyboard.is_pressed('s+a'):
            move_backLeft(simCon)
        
        elif keyboard.is_pressed('s+d'):
            move_backRight(simCon)
        
        else:
            resetStick(simCon)



main()