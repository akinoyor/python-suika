import math
import random
BOARD_SIZE = 10
suika_x = random.randrange(0, BOARD_SIZE)
suika_y = random.randrange(0, BOARD_SIZE)
player_x = random.randrange(0, BOARD_SIZE)
player_y = random.randrange(0, BOARD_SIZE)

CLEAR_MESSAGE = 'Congratulations on the correct answer'

while (player_x != suika_x)or(player_y != suika_y):
    dx = suika_x - player_x
    dy = suika_y - player_y
    distance = math.sqrt(dx**2 + dy**2)
    print('プレイヤーとスイカの距離',distance)
    move = input('N:北へ一歩　E:東へ一歩　S:南へ一歩　W:西へ一歩 どちらに動くか入力してください')
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

print(CLEAR_MESSAGE)
