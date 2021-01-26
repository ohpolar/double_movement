import pyvjoy, keyboard
import joystick

def main():
    # infinite loop that detects for ('w+a') or ('w+d') in order to apply double movement
    while True:

        if keyboard.is_pressed('w+a'):
            joystick.move_left()
        
        if keyboard.is_pressed('w+d'):
            joystick.move_right()



if __name__ == '__main__':
    main()