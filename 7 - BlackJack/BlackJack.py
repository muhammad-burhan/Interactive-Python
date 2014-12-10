# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
player_hand = []
dealer_hand = []
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
mess= ""
back = True

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        #empty list of card object
        self.hand = [] 
        
    def __str__(self):
        ans = ""
        for i in range(len(self.hand)):
            ans += " " + str(self.hand[i])
        return "Hand contains" + ans

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        hand_value = 0
        for i in range(len(self.hand)):
            hand_value += VALUES[self.hand[i].rank]
            if(self.hand[i].rank == 'A'):
                if(hand_value + 10 <= 21):
                    hand_value += 10        
        return hand_value
   
    def draw(self, canvas, pos):
        for c in self.hand:
            c.draw(canvas, pos)
            pos[0] += 80
        
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        ans = ""
        for i in range(len(self.deck)):
            ans += " " + str(self.deck[i])
        return "Deck contains" + ans

#define event handlers for buttons
def deal():
    global outcome, in_play, new_deck, mess
    mess = ""
    outcome = ""
    if (in_play == True):
        mess = "Player lose the round! Click Deal"
        print mess
        in_play = False
    else:
        new_deck = Deck()
        new_deck.shuffle()
        global player_hand, dealer_hand
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(new_deck.deal_card())
        dealer_hand.add_card(new_deck.deal_card())
        print "*****************New Deal***********************"
        print "Player " + str(player_hand)
        print "Dealer "+ str(dealer_hand)
        in_play = True

def hit():
    global player_hand, dealer_hand, score, outcome, in_play, mess
    if(in_play == True):
        if(player_hand.get_value()<=21):
            player_hand.add_card(new_deck.deal_card())
        print "Player " + str(player_hand)
        print "Dealer "+ str(dealer_hand)
        if(player_hand.get_value() > 21):
            outcome = "You have busted, New Deal?"
            score -= 1
            in_play = False
            print str(outcome) + " score is " + str(score)
        else: 
            mess = "Hit or stand?"
            print mess
    else:
        print "Please click the deal button"
       
def stand():
    global player_hand, dealer_hand, score, outcome, in_play, back
    #dealer's card Faceup/down check
    back = False
    if (in_play == False):
        print "Please click the deal button"
    else:
        #Hitting dealer while 17
        while(dealer_hand.get_value() < 17):
            dealer_hand.add_card(new_deck.deal_card())
        print "Player " + str(player_hand)
        print "Dealer "+ str(dealer_hand)
        #Testing conditions
        if(dealer_hand.get_value() > 21):
            outcome = "Dealer Busted, You win. New Deal?"
            in_play = False
            score += 1
        elif(player_hand.get_value()<= dealer_hand.get_value()):
            outcome = "Dealer Wins, New Deal?"
            in_play = False
            score -= 1
        else:
            outcome = "Player Won, New round?"
            score += 1
            in_play = False
            #printing score
        print str(outcome) + " score is " + str(score)


# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Black Jack', (30, 50), 40, 'White')
    canvas.draw_text("Score " + str(score), (400, 50), 30, 'Black')
    canvas.draw_text(str(outcome), (100, 100), 28, 'Red')
    canvas.draw_text(str(mess), (100, 150), 20, 'White')
    canvas.draw_text("Dealer", (100, 200), 40, 'White')
    canvas.draw_text("Player", (100, 400), 40, 'White')
    player_hand.draw(canvas, [100, 420])
    dealer_hand.draw(canvas, [100, 220])

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric