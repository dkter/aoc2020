from collections import deque
from itertools import islice

players = {}
with open("day22.in") as f:
    for line in f:
        if ":" in line:
            player_name = line.strip(":\n")
            players[player_name] = deque()
        elif line.strip():
            players[player_name].append(int(line.strip()))

p1 = "Player 1"
p2 = "Player 2"

def play(p1_score, p2_score):
    scores = set()
    while p1_score and p2_score:
        a, b = p1_score.popleft(), p2_score.popleft()
        if (tuple(p1_score), tuple(p2_score)) in scores:
            # make sure the win state is clear
            if not p1_score:
                p1_score = True
            p2_score = False
            break
        scores.add((tuple(p1_score), tuple(p2_score)))

        if a <= len(p1_score) and b <= len(p2_score):
            result_p1, result_p2 = play(
                deque(islice(p1_score, 0, a)),
                deque(islice(p2_score, 0, b))
            )
            if not result_p1:
                p2_score.append(b)
                p2_score.append(a)
            else:
                p1_score.append(a)
                p1_score.append(b)
        elif a > b:
            p1_score.append(a)
            p1_score.append(b)
        else:
            p2_score.append(b)
            p2_score.append(a)
    return p1_score, p2_score

players[p1], players[p2] = play(players[p1], players[p2])

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
