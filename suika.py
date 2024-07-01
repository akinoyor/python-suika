import math
import random
suikaX = random.randrange(0, 10)
suikaY = random.randrange(0, 10)
playerX = random.randrange(0, 10)
playerY = random.randrange(0, 10)

clearMessage = 'Congratulations on the correct answer'

while (playerX != suikaX)or(playerY != suikaY):
    dx = suikaX - playerX
    dy = suikaY - playerY
    distance = math.sqrt(dx**2 + dy**2)
    print('プレイヤーとスイカの距離',distance)
    move = input('N:北へ一歩　E:東へ一歩　S:南へ一歩　W:西へ一歩 どちらに動くか入力してください')
    if(move == 'N'):
        playerY = playerY + 1
    elif(move == 'E'):
        playerX = playerX + 1
    elif(move == 'S'):
        playerY = playerY - 1
    elif(move == 'W'):
        playerX = playerX - 1
    else:
        print('大文字のNESWで入力してください')

print(clearMessage)
