#%% Day 20
from collections import namedtuple

def get_pos(place, die):
    s, die = get_die_sum(die)
    return ((place+s)%10 or 10), die
    
def get_die_sum(die):
    d1= die     % 100 or 100
    d2= (die+1) % 100 or 100
    d3= (die+2) % 100 or 100
    print('rolls:',d1,d2,d3)
    s = d1 + d2 + d3

    return s, ((die +3)%100 or 100)


def one_iter(player, p, die, score):    
    pos, die = get_pos(p[player], die)
    score[player] += pos
    p[player] = pos
    #print(f"Player {player} rolls  and moves to space {pos} for a total score of {score[player]}.")
    return player, p, die,score

Game_stats = namedtuple('Game', ['p', 'score', 'die', 'c', 'tosses', 'limit'])
stats = Game_stats(p={1:4, 2:8}, score={1:0,2:0}, die=1, c=1, tosses=0, limit=1000)

def game(stats):    
    tosses = stats.tosses
    c = stats.c
    p = stats.p
    score = stats.score
    die = stats.die

    while score[1]<=stats.limit and score[2] <=stats.limit:
        player = c%2 or 2
        player, p, die, score = one_iter(player, p, die, score)
        tosses += 3
        c+=1        

        if score[player]>=stats.limit:        
            return score[1+1%2 or 2]*tosses
        
'task1', game(stats)

# %%
