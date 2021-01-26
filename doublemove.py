import pyvjoy, keyboard

def main():
    # infinite loop that detects for ('w+a') or ('w+d') in order to apply double movement
    while True:

        if keyboard.is_pressed('w+a'):
            move_left()
        
        if keyboard.is_pressed('w+d'):
            move_right()



if __name__ == '__main__':
    main()