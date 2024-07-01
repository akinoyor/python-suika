import math
import random
suikaX = random.randrange(0, 10)
suikaY = random.randrange(0, 10)
playerX = random.randrange(0, 10)
playerY = random.randrange(0, 10)
suika = [suikaX, suikaY]#仮設定　最終的にはRandamを用いて行う
player = [playerX, playerY]#プレイヤー初期値
clearMessage = 'Congratulations on the correct answer'

print(player == suika)
while player != suika:
    dx = suika[0] - player[0]
    dy = suika[1] - player[1]
    print(dx, dy)
    distance = math.sqrt(dx**2 + dy**2)
    print(distance)

print(clearMessage)
