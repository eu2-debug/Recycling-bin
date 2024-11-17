import pgzrun
import random

WIDTH = 800

HEIGHT = 600

CENTRE_X = WIDTH / 2

CENTRE_Y = HEIGHT / 2

CENTRE = (CENTRE_X, CENTRE_Y)

FINAL_LEVEL = 6

START_SPEED = 12

ITEMS = ["bag","battery","bottle","chips"]



game_over = False

game_complete = False

current_level = 1

# bag = Actor("paperimg")

items = []

animations = []

def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("bground",(0,0))
    if game_over == True:
        display_message("GAME OVER")
    elif game_complete == True:
        display_message("You are a recycler!")
    else:
        for item in items:
            item.draw()
            
def update():
    global items 
    if len(items) == 0:
        items = make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items
    
def get_option_to_create(number_of_extra_items):
    items_to_create = ["paper"]
    for i in range(0,number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create
     
     #creating items for the game
def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option+"img")
        new_items. append(item)
    return new_items
    
    
        
 
















pgzrun.go()
