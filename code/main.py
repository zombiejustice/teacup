########################
#                      #
#  teacup main module  #
#                      #
########################

### imports ###
import libtcodgui as gui

### the game state ###

class GameState():
#a class whose instances hold all the strings
#of the various parts of the game state,
#eg. the map chunks, the critters, &c.

    def __init__(self):
    #constructor
    #this version of the constructor is for a New Game
    
        self.pc = 0 #placeholder until critters
        
        #chunk octants
        #upper four are absent for now
        self.lne = []
        self.lnw = []
        self.lsw = [] 
        self.lse = []
    
        #for later: put map generation call here
    #end constructor for new games
    
#end GameState

class Entity():
# a class to represent objects which
# 'live or move or have their being'
# eg. critters, tools, corpses,
# furniture, and consumables
    
    def __init__(self, state, entity_type, pos, blocking=False, heart=None, body=None, soul=None, canta=None):
    #Entity constructor
    #takes a state reference, an entity_type and position, preferrably a blocking flag,
    #and optionally a heart, body, soul, or canta
        self.state = state
        self.entity_type = entity_type
        self.pos = pos
        self.blocking = blocking
        self.heart = heart
        self.body = body
        self.soul = soul
        self.canta = canta
        return_ok
    
    def move(self, delta):
        #moves a critter, if possible
        #takes a 2-delta
        #returns success boolean
        if self.entity_type is 0: #critters
            return True
        else:
            return False
    
    
    
### set-up ###


#for later: put GUI preference file loading here
success = gui.window_init()
if not success:
    gui.get_errors()
    
#for later: put game state loading here
if True: #placeholder until conditional newgame generation
    game = GameState()

#interaction mode determines pace and applicable actions
#exit means shut it down
#crawl is for dungeon delving
#crawl-look is for examining things for free in RL mode
interaction_mode = 'crawl'
while interaction_mode is not 'exit':
    #for later: get game state relevant to interaction_mode
    #for later: send gui relevant infor to display
    #get action from gui
    action = gui.get_action()
    #respond to action
    if action[0] is 'quit':
        interaction_mode = 'exit'
    elif action[0] is 'toggle_fullscreen':
        #this returns a boolean, but we're not using it yet
        gui.toggle_fullscreen()
    elif action[0] is 'toggle_dvorak':
        #this returns a boolean, but we're not using it yet
        gui.toggle_dvorak()

#end while
    
