
import mouse
from time import sleep
import sys
import keyboard
import random
import pyautogui
import threading


def main():

    print('\nTo end the program : press Q for 3 sec')
    print(' Starting bot in 5 sec ')
    print()
    sleep(4)  # lol

    # check if valorant is active than run
    try:
        focusOnValorant()
        # came here means valo is active and chat_afk() function executed
        chat_afk()
        global bot_flag
        bot_flag = True  # will be used to terminate the bot / thread
        # creating thread || yes u can pass function XD
        t1 = threading.Thread(target=no_afk)
        # starting thread || calling no_afk in parallel
        t1.start()
        while bot_flag == True:
            sleep(3)
            if keyboard.is_pressed('q'):
                chat_nafk()
                bot_flag = False
                
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
    sleep(0.5)
    keyboard.press_and_release('enter')
    sleep(1)
    pyautogui.typewrite('This kid got small ego n is pissed')
    sleep(0.5)
    keyboard.press_and_release('enter')
    keyboard.press_and_release('enter')
    sleep(0.5)
    pyautogui.typewrite('he\'s gone AFK. So this cute bot will play GG')
    sleep(0.5)
    keyboard.press_and_release('enter')

def chat_nafk():
    sleep(0.5)
    keyboard.press_and_release('enter')
    sleep(1)
    pyautogui.typewrite('This mf kid is back!')
    sleep(0.5)
    keyboard.press_and_release('enter')
    keyboard.press_and_release('enter')
    sleep(0.5)
    pyautogui.typewrite('I gotta go :), Play with shit kid!')
    sleep(0.5)
    keyboard.press_and_release('enter')
# end of chat function


def click():
    sleep(1)
    mouse.wheel(-1)
    mouse.wheel(1)
    pyautogui.click()
    mouse.wheel(-1)
    mouse.wheel(1)


def Shoot(x, y):
    mouse.drag(0,0,x, y, absolute=False, duration=1)
    pyautogui.click()


pyautogui.FAILSAFE = False


def no_afk():
    # print('hello world')
    sleep(0.5)
    while bot_flag == True:

        posx = random.randint(-500, 500)
        posy = random.randint(-500, 500)

        choice = random.randint(1, 12)  # 1 to wa10
        sleeptime = random.randint(1, 10)
        # sed lyf no switch case :(
        Shoot(posx, posy)

        # W
        if choice == 1:
            keyboard.press('w')
            sleep(sleeptime)
            keyboard.release('w')

            keyboard.press('b')
            keyboard.release('b')
            sleep(1)
            pyautogui.click(900, 664)

        # A
        elif choice == 2:
            keyboard.press('a')
            sleep(sleeptime)
            keyboard.release('a')
        # S
        elif choice == 3:
            keyboard.press('s')
            sleep(sleeptime)
            keyboard.release('s')

            keyboard.press('b')
            keyboard.release('b')
            sleep(1)
            pyautogui.click(900, 664)
        # D
        elif choice == 4:
            keyboard.press('d')
            sleep(sleeptime)
            keyboard.release('d')
        # jump
        elif choice == 5:
            keyboard.press('space')
            sleep(sleeptime)
            keyboard.release('space')

            keyboard.press('b')
            keyboard.release('b')
            sleep(1)
            pyautogui.click(900, 664)
        # crouch
        elif choice == 6:
            keyboard.press('control')
            sleep(sleeptime)
            keyboard.release('control')

        elif choice == 7:
            for i in range(sleeptime):
                click()

        elif choice == 8:
            keyboard.press('w')
            keyboard.press('a')
            sleep(sleeptime)
            keyboard.release('w')
            keyboard.release('a')

        elif choice == 9:
            keyboard.press('w')
            keyboard.press('d')
            sleep(sleeptime)
            keyboard.release('w')
            keyboard.release('d')

        elif choice == 10:
            keyboard.press('b')
            keyboard.release('b')
            sleep(1)
            pyautogui.click(900, 664)
            keyboard.press('b')
            keyboard.release('b')
        elif choice == 11:
            keyboard.press('e')
            keyboard.release('e')
            sleep(1)
            pyautogui.click(900, 664)
            keyboard.press('3')
            keyboard.release('3')

        elif choice == 12:
            keyboard.press('c')
            keyboard.release('c')
            sleep(1)
            pyautogui.click(900, 664)
            keyboard.press('1')
            keyboard.release('1')

        # lets have some fun
        # lOL
        # elif choice == 7: #lol
        #     keyboard.press_and_release('enter')
        #     sleep(1)
        #     pyautogui.typewrite(' LOL :)')
        #     sleep(2)
        #     keyboard.press_and_release('enter')
        #     # sleep(sleeptime)
        # # afk
        # elif choice == 8:
        #     keyboard.press_and_release('enter')
        #     sleep(2)
        #     pyautogui.typewrite('Sorry boiz Im AFK')
        #     sleep(1)
        #     keyboard.press_and_release('enter')
        #     sleep(sleeptime)
        # 9) buy gun
        # 10) do something
    # end of while loop
# end of afk function wwds


# ******** Main Function ********** #
# calling main function
if __name__ == "__main__":
    main()
