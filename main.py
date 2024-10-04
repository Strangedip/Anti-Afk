
import mouse
from time import sleep
import sys
import keyboard
import random
import pyautogui
import threading


def main():

    print('\nTo end the program : press . for 1 sec')
    print(' Starting bot in 5 sec ')
    print()
    sleep(4)  # lol

    # check if valorant is active than run
    try:
        focusOnValorant()
        sleep(1)
        # came here means valorant is active and chat_afk() function executed
        chat_afk()
        global bot_flag
        bot_flag = True  # will be used to terminate the bot / thread
        # creating thread || yes u can pass function XD
        t1 = threading.Thread(target=no_afk)
        # starting thread || calling no_afk in parallel
        t1.start()
        while bot_flag == True:
            sleep(1)
            if keyboard.is_pressed('.'):
                bot_flag = False    
                chat_nafk()
                sys.exit()
                return
        # end of try block
    except:
        print()
        # thinking...

    print('\n       THATS DONE!!    ')

# end of main function


def focusOnValorant():
    # get list of active windows with name = VALORANT
    list = pyautogui.getWindowsWithTitle('VALORANT')
    # check
    if len(list) == 0:
        print('\n   Valorant is Not active')
        print('Exiting in 5 sec ', end='')
        for i in range(4):  # lol
            sleep(1)
            print('. ', end='')
        sys.exit()
    else:
        valorant = list[0]
        if valorant.isMinimized == True:
            valorant.restore()  # run
            # chat_afk()
# end of focus function

def chat_afk():
    keyboard.press_and_release('enter')
    sleep(0.2)
    pyautogui.typewrite('This kid got small ego n is pissed')
    sleep(0.2)
    keyboard.press_and_release('enter')
    sleep(0.2)
    keyboard.press_and_release('enter')
    sleep(0.2)
    pyautogui.typewrite('he\'s gone AFK and will use his time in learning something!')
    sleep(0.2)
    keyboard.press_and_release('enter')
    sleep(0.2)
    keyboard.press_and_release('enter')
    sleep(0.2)
    pyautogui.typewrite('So now this cute AI will play with you :) Dont worry i am harmless!')
    sleep(0.2)
    keyboard.press_and_release('enter')

def chat_nafk():
    keyboard.press_and_release('enter')
    sleep(0.7)
    pyautogui.typewrite('This mf ego kid is back! cant play with you')
    sleep(0.7)
    keyboard.press_and_release('enter')
    sleep(0.7)
    keyboard.press_and_release('enter')
    sleep(0.7)
    pyautogui.typewrite('I gotta go :)')
    sleep(0.7)
    keyboard.press_and_release('enter')
# end of chat function


def click():
    sleep(1)


def Shoot(x, y):
    mouse.drag(0,0,x, y, absolute=False, duration=1)
    # pyautogui.click()
    


def start():
    sleep(2)
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width / 2 
    center_y = screen_height - 90
    pyautogui.moveTo(center_x, center_y)
    sleep(0.5)
    # mouse.drag(0,0,0, 450, absolute=False, duration=1)
    pyautogui.click()
    sleep(10)
    select_agent()

def select_agent():
    sleep(2)
    screen_width, screen_height = pyautogui.size()
    center_x = (screen_width / 2 )-750
    center_y = (screen_height/2)-130
    pyautogui.moveTo(center_x, center_y)
    sleep(0.5)
    # mouse.drag(0,0,0, 450, absolute=False, duration=1)
    pyautogui.click()

def close_invite_panel():
    sleep(2)
    screen_width, screen_height = pyautogui.size()
    center_x = (screen_width / 2 )+250
    center_y = (screen_height/2)-100
    pyautogui.moveTo(center_x, center_y)
    sleep(0.5)
    # mouse.drag(0,0,0, 450, absolute=False, duration=1)
    pyautogui.click()


pyautogui.FAILSAFE = False


def no_afk():
    # To stop the bot, you would need some logic to set bot_flag to False

    while bot_flag:
        posx = random.randint(-500, 500)
        posy = random.randint(-500, 500)

        choice = random.randint(1, 20)  # Updated range to 15 for more actions
        sleeptime = random.randint(1, 10)


        # Example of a shoot function, replace it with your actual implementation
        if choice%4==0 and sleeptime%2==0:
            start()
        elif choice%2==0:
            select_agent()
        
        Shoot(posx, posy)

        # Move Forward
        if choice == 1:
            keyboard.press('w')
            sleep(sleeptime)
            keyboard.release('w')
        
        # Move Left
        elif choice == 2:
            keyboard.press('a')
            sleep(sleeptime)
            keyboard.release('a')
        
        # Move Backward
        elif choice == 3:
            keyboard.press('s')
            sleep(sleeptime)
            keyboard.release('s')
        
        # Move Right
        elif choice == 4:
            keyboard.press('d')
            sleep(sleeptime)
            keyboard.release('d')
        
        # Move Forward + Left (Diagonal)
        elif choice == 5:
            keyboard.press('w')
            keyboard.press('a')
            sleep(sleeptime)
            keyboard.release('w')
            keyboard.release('a')
        
        # Move Forward + Right (Diagonal)
        elif choice == 6:
            keyboard.press('w')
            keyboard.press('d')
            sleep(sleeptime)
            keyboard.release('w')
            keyboard.release('d')
        
        # Move Backward + Left (Diagonal)
        elif choice == 7:
            keyboard.press('s')
            keyboard.press('a')
            sleep(sleeptime)
            keyboard.release('s')
            keyboard.release('a')
        
        # Move Backward + Right (Diagonal)
        elif choice == 8:
            keyboard.press('s')
            keyboard.press('d')
            sleep(sleeptime)
            keyboard.release('s')
            keyboard.release('d')
        
        # Jump
        elif choice == 9:
            keyboard.press_and_release('space')        

        # Crouch
        elif choice == 10:
            keyboard.press('control')
            sleep(sleeptime)
            keyboard.release('control')

        # Sprint (e.g., Shift key held down for running)
        elif choice == 11:
            keyboard.press('shift')
            sleep(sleeptime)
            keyboard.release('shift')

        # Interaction (e.g., 'e' to interact or open menu)
        elif choice == 12:
            keyboard.press('e')
            sleep(sleeptime)
            keyboard.release('e')

        # Reload (e.g., 'r')
        elif choice == 13:
            keyboard.press('r')
            sleep(sleeptime)
            keyboard.release('r')

        elif choice == 15:
            keyboard.press('q')
            sleep(sleeptime)
            keyboard.release('q')
        elif choice == 16:
            keyboard.press_and_release('c')
        elif choice == 17:
            keyboard.press_and_release('q')
        elif choice == 18:
            keyboard.press_and_release('1')
        elif choice == 19:
            keyboard.press_and_release('2')

        sleep(0.3)


# ******** Main Function ********** #
# calling main function
if __name__ == "__main__":
    main()

