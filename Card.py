#
import random
suits=('hearts','diamond','spade','black')
ranks=('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':11,'queen':12,'king':13,'ace':14}   

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank.lower()]
    def __str__(self):
        return self.rank +'of'+ self.suit    
class Deck:
    def __init__(self):
        self.all_card=[]
        for suit in suits:
            for rank in ranks:
                 card=Card(suit,rank)

                 self.all_card.append(card) 
    def shuffle(self):
        random.shuffle(self.all_card)
    def deal_one(self):
         return self.all_card.pop()    
class Player:

    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_one(self,new_card):
        if type(new_card)==type([]):
            return self.all_cards.extend(new_card)
        else:
            return self.all_cards.append(new_card)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
    
### GAME SETUP ###
print('Welcome!')
name1=input('Name of player one:')
name2=input('Name of player two:')
player_one=Player(name1)
player_two=Player(name2)
new_deck=Deck()
new_deck.shuffle()
###DISTRIBUTION OF CARDS###
for i in range (26):
    player_one.add_one(new_deck.deal_one())
    player_two.add_one(new_deck.deal_one())

game_on=True
round=0
while game_on:
    round+=1
    print(round)
    #check whether someone is winnner
    if len(player_one.all_cards)==0:
        print(f'{player_one.name} is oout of card!!')
        print(f'{player_two.name} Won!!')
    if len(player_two.all_cards)==0:
        print(f'{player_two.name} is out of cards!!')
        print(f'{player_one.name} Won!!')    
    #
    # START A NEW ROUND   
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one()) 
    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())
    war=True
    while war:
        if player_one_cards[-1].value >player_two_cards[-1].value :
            player_one.add_one(player_one_cards)
            player_one.add_one(player_two_cards)
            war=False
        elif player_two_cards[-1].value >player_one_cards[-1].value :
            player_two.add_one(player_one_cards)
            player_two.add_one(player_two_cards)
            war=False   
        else:
            print('WAR!!!')
            if len(player_one_cards)<5:
                print(f'{player_one.name} is not able to declare war...')
                print(f'{player_two.name}WINS!!!')
                game_on=False
                break
            elif len(player_two_cards)<5:
                print(f'{player_two.name} is not able to declare war...')
                print(f'{player_one.name}WINS!!') 
                game_on=False 
                break 
            else:
                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())

        
