import math
import random
BOARD_SIZE = 10
CLEAR_MESSAGE = 'Congratulations on the correct answer'

def generate_position(size):
    x = random.randrange(0, size)
    y = random.randrange(0, size)
    return (x, y)

def suika_player_distance(suika, player):
    dx = suika[0] - player[0]
    dy = suika[1] - player[1]
    return math.sqrt(dx**2 + dy**2)

def move_direction(player):
    move = input('N:北へ一歩　E:東へ一歩　S:南へ一歩　W:西へ一歩 どちらに動くか入力してください')
    player_x, player_y = player
    if(move == 'N'):
        player_y = player_y + 1
    elif(move == 'E'):
        player_x = player_x + 1
    elif(move == 'S'):
        player_y = player_y - 1
    elif(move == 'W'):
        player_x = player_x - 1
    else:
        print('大文字のNESWで入力してください')
    return(player_x, player_y)

def suika_wari():
    suika = generate_position(BOARD_SIZE)
    player = generate_position(BOARD_SIZE)
    while (player != suika):
        distance = suika_player_distance(suika, player)
        print('プレイヤーとスイカの距離', distance)
        player = move_direction(player)
    print(CLEAR_MESSAGE)
