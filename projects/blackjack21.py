#  колода из 36 карт, перемешанная в случайном порядке

# ри взятии карты прибавляет ее номинал к своим очкам

# взятая карта удаляется из колоды

# побеждает тот игрок, который набрал 21 очко

# если никто не набрал 21, побеждает тот, кто набрал ближе к 21
import random
def setup_deck():
    deck = [2,3,4,6,7,8,9,10,11]*4
    random.shuffle(deck)
    print(deck)
    return deck
 
def draw_a_card(deck):
    if len(deck) !=0:
       card = deck.pop(-1) 
    else:
        card = None
    return card
def update_score(current_score, score_amount):
    current_score = current_score + score_amount
    return current_score

def count_score(score):
    if score == 21:
        return True
    elif score >21:
        return False
    elif score <21:
         return None
def draw_decision(text):
    if text == 'y':
      return True
    elif text == 'n':
      return False
    else:
        return None

def setup_players(num_players =1):
    list_of_players = []
    for i in range(1,num_players+1):
        player = {'name':f'Player N{i}',
        'score':0,
        'is_bot':False,
        'is winner':False}
        list_of_players.append(player)
    print(list_of_players)
    return(list_of_players)

def choose_winner(players):
    winners = []
    win_score = []
    for player in players:
        if player['is winner'] == True:
         return player['name']
        elif player['score'] <21:
            win_score.append(player['score'])
            winners.append(player)
    print(winners)
    win_score.sort()
    if winners:
        for player in winners:
            if player['score']== win_score[-1]:
                return player['name']
    else:
        return 'Нет победителя!'

s_deck = setup_deck()
while True:
    num_players = input('Vvedite kolichestvo igrokov')
    try:
        num_players = int(num_players)
        answer = 1/num_players
        print('succes!')
    except ZeroDivisionError:
        print('write a new number, cannot divide by zero!')
    except ValueError:
        print('enter only numbers!')
    else:
        break

players = setup_players(num_players)


for active_player in players:
    players_score = active_player['score']
    b_continue = True
    while b_continue:

        d_card = draw_a_card(s_deck)
        if d_card != None:
            print('Вы вытянули: ',d_card)
            players_score = update_score(players_score,d_card)
            print(f'У вас {players_score} очков')
            b_win = count_score(players_score)
            if b_win == None:
                pass
            elif b_win == False:
                print('Вы проиграли!')
                break
            elif b_win == True:
                print('Вы победили!')
                active_player['is winner'] = True
                break
            

        else:
            print('Колода закончилась')
            break
        while True:
            desicion = input('Berem eshe kartu: ')
            b_continue = draw_decision(desicion)
            if b_continue == None:
                print('Неверная команда')
                continue
            break
    else:
        print(f'Вы закончили игру с {players_score} очков')
    active_player['score'] = players_score
print(players)
print(choose_winner(players))
print('До новых встреч')


