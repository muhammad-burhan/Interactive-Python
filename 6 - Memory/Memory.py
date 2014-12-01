# implementation of card game - Memory

import simplegui
import random
list1 = range(0,8)
list2 = range(0,8)
list3 = list1 + list2
exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
CARD_WIDTH = 50
CARD_HEIGHT = 100
card1 = -1
card2 = -1
card1_index = -1
card2_index = -2
Count = 0
# helper function to initialize globals
def new_game():
    global exposed, state, Count
    state = 0
    Count = 0
    random.shuffle(list3)
    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    label.set_text("Turns = " + str(Count)) 
# define event handlers
def mouseclick(pos):
    global exposed, state, card1, card2, card1_index, card2_index, Count
    
    # add game state logic here
    if (pos[0] <= 50):
        index = 0
    elif ((pos[0] > 50) and (pos[0] <= 100)):
        index = 1
    elif ((pos[0] > 100) and (pos[0] <= 150)):
        index = 2
    elif ((pos[0] > 150) and (pos[0] <= 200)):
        index = 3
    elif ((pos[0] > 200) and (pos[0] <= 250)):
        index = 4
    elif ((pos[0] > 250) and (pos[0] <= 300)):
        index = 5
    elif ((pos[0] > 300) and (pos[0] <= 350)):
        index = 6
    elif ((pos[0] > 350) and (pos[0] <= 400)):
        index = 7
    elif ((pos[0] > 400) and (pos[0] <= 450)):
        index = 8
    elif ((pos[0] > 450) and (pos[0] <= 500)):
        index = 9
    elif ((pos[0] > 500) and (pos[0] <= 550)):
        index = 10
    elif ((pos[0] > 550) and (pos[0] <= 600)):
        index = 11
    elif ((pos[0] > 600) and (pos[0] <= 650)):
        index = 12
    elif ((pos[0] > 650) and (pos[0] <= 700)):
        index = 13
    elif ((pos[0] > 700) and (pos[0] <= 750)):
        index = 14
    elif ((pos[0] > 750) and (pos[0] <= 800)):
        index = 15
    
    if (exposed[index] == False):
        if(state == 0):
            exposed[index] = True
            state = 1
            card1 = list3[index]
            card1_index = index
        elif(state == 1):
            exposed[index] = True
            state = 2
            card2 = list3[index]
            card2_index = index
            Count += 1
        elif(state == 2):
            if(card1 == card2):
                print "matched"
            else:
                exposed[card1_index] = False
                exposed[card2_index] = False
            exposed[index] = True
            card1 = list3[index]
            card1_index = index
            state = 1
    label.set_text("Turns = " + str(Count))
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    width_text = 15
    for num in range(0, len(list3)):
        text = str(list3[num])
        canvas.draw_text(text, [width_text, 65], 50, "Red")
        width_text += 50
        if (exposed[num] == False):
            canvas.draw_polygon([(CARD_WIDTH * num, 0), 
                            ((CARD_WIDTH * num) + CARD_WIDTH, 0), 
                            ((CARD_WIDTH * num) + CARD_WIDTH, CARD_HEIGHT), 
                            (CARD_WIDTH * num, CARD_HEIGHT)], 
                            1, "Black", "Green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(Count))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

