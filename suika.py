import math

suika = [10, 10]#仮設定　最終的にはRandamを用いて行う
player = [7, 6]#プレイヤー初期値
clearMessage = 'Congratulations on the correct answer'
print(player == suika)
if player == suika:
    print(clearMessage)
else:
    dx = suika[0] - player[0]
    dy = suika[1] - player[1]
    print(dx, dy)
    distance = math.sqrt(dx**2 + dy**2)
    print(distance)