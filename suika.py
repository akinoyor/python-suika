import math
import random
BOARD_SIZE = 10
suika = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE))
player = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE))

CLEAR_MESSAGE = 'Congratulations on the correct answer'

while (player != suika):
    dx = suika[0] - player[0]
    dy = suika[1] - player[1]
    distance = math.sqrt(dx**2 + dy**2)
    print('プレイヤーとスイカの距離', distance)
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
    
    player = (player_x, player_y)

print(CLEAR_MESSAGE)
