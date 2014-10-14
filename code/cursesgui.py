#######################
#                     #
#  teacup gui module  #
#  using curses *     #
#                     #
#######################

# *currently being adapted from libtcodgui


### imports ###

#import curses
import curses


### error buffer ###

#a list of error strings
error_buffer = []

def get_errors():
#takes nothing, returns nothing
#prints all the errors in the error buffer to standard out

    for s in error_buffer:
        print(s)

#end get_errors
        
def put_error(s):
#takes a string, returns nothing
#puts an error message in the error buffer
    global error_buffer
    error_buffer.append(str(s))
    return
        
#end put_error


### globals ###

assume_dvorak = True #assumes that user's keyboard is in dvorak by default


### set-up ###

def window_init(fullscreen = False):
#takes a boolean flag, fullscreen, ignored in curses
#returns True if no errors, o/w False
#inits the console

    #init the console
    global stdscr
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)

    return True

#end window_init

### gui adjustments ###

def toggle_fullscreen():
#takes nothing
#returns False, in curses
    return False    
#end toggle_fullscreen
    
def toggle_dvorak():
#takes nothing
#returns True if key handler is now in dvorak, False o/w
#toggles the key handler between dvorak and qwerty
    global assume_dvorak
    assume_dvorak = not assume_dvorak
    return assume_dvorak
#end toggle_dvorak


### user input ###

def get_action():
#takes nothing
#returns action string
#handles keys, basically
    if libtcod.console_is_window_closed():
        #check for window close event before keypresses
        return ['quit']
    key = libtcod.console_wait_for_keypress(True)
    #quit
    if key.vk == libtcod.KEY_ESCAPE:
        return ['quit']
    #fullscreen
    if key.vk == libtcod.KEY_F11:
        return ['toggle_fullscreen']
    #only characters from this point
    if key.c == 0:
        put_error("keypress not defined error")
        return ['error']
    keychar = chr(key.c)
    
    if keychar == 'q':     
        return ["look"]
    #movement
    if keychar == 't':
        return ["move", [0, -1]]
    elif keychar == 'h':
        return ["move", [0, 1]]
    elif keychar == 'd':
        return ["move", [-1, 0]]
    elif keychar == 'n':
        return ["move", [1, 0]]
    elif keychar == 'f':
        return ["move", [-1, -1]]
    elif keychar == 'g':
        return ["move", [1, -1]]
    elif keychar == 'x':
        return ["move", [-1, 1]]
    elif keychar == 'b':
        return ["move", [1, 1]]
    
    #if all else fails
    return "none"
    
def debug_print(msg):
#takes a msg to print
#returns nothing
#prints immediately
    print(msg)
    
def debug_input():
#takes nothing, returns a char
#turns all non-char inputs to '0'
    return 0  
