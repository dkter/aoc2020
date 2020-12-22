from collections import deque

players = {}
with open("day22.in") as f:
    for line in f:
        if ":" in line:
            player_name = line.strip(":\n")
            players[player_name] = deque()
        elif line.strip():
            players[player_name].append(int(line.strip()))

scores = {player_name: 0 for player_name in players}
p1 = "Player 1"
p2 = "Player 2"
done = False
while not done:
    a, b = players[p1].popleft(), players[p2].popleft()
    if a > b:
        players[p1].append(a)
        players[p1].append(b)
    elif b > a:
        players[p2].append(b)
        players[p2].append(a)
    else:
        print("tie")
    print(players)
    if not players[p1] or not players[p2]:
        done = True

if not players[p1]:
    winner = p2
elif not players[p2]:
    winner = p1
else:
    print("hmm")

score = sum(
    score * multiplier
    for score, multiplier in zip(players[winner], range(len(players[winner]), 0, -1))
)

print(score)
