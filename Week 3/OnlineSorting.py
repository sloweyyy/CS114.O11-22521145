online_players = {}

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    elif arr[0] == 1:
        online_players[arr[1]] = 1
    elif online_players.get(arr[1]):
        sorted_players = sorted(online_players.keys())
        position = sorted_players.index(arr[1]) + 1
        print(position)
    else:
        print(0)
