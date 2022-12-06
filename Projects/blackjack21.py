# колода из 36 карт, перемешанная в случайном порядке

# при взятии карты игрок прибавляет ее номинал к своим очкам

# взятая карта удаляется из колоды

# побеждает тот игрок, который набрал 21 очко

# если никто не набрал 21, побеждает тот, кто набрал ближе всего к 21 
import random

def setup_deck():
    deck = [2,3,4,6,7,8,9,10,11]*4
    random.shuffle(deck)
    return deck
    print(deck)

def draw_a_card(deck):
    if len(deck) != 0:  # if deck:
        card = deck.pop(-1)
    else:
        card = None    
    return card

def update_score(current_score, score_amount):
    current_score = current_score + score_amount # current_score += score_amount
    return current_score

def count_score(score):
    if score == 21:
        return True
    elif score > 21:
        return False
    elif score < 21:
        return None
def draw_decision(text):
    if text == 'y':
        return True
    elif text == 'n':
        return False
    else:
        return None       

s_deck = setup_deck()
player_score = 0 
b_continue = True
while b_continue:

    d_card = draw_a_card(s_deck)
    if d_card != None : # if d_card:
        print('Вы вытянули:',d_card)
        player_score = update_score(player_score,d_card)
        print(f'У вас {player_score} очков')
        b_win = count_score(player_score)
        if b_win == None:
            pass
        elif b_win == False:
            print('Вы проиграли!')
            break
        elif b_win == True:
            print('Вы победили!')
            break    
    else:
        print('Колода закончилась!')
        break
    decision = input('Берем еще карту?\ny/n \n')
    b_continue = draw_decision(decision)
    if b_continue == None:
        print("Неверная команда")
else:
    print(f'Вы закончили игру с {player_score} очков')        
print('До новых встреч!')    