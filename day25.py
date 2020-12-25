from itertools import count
from sympy.ntheory.residue_ntheory import discrete_log

mod = 20201227

with open("day25.in") as f:
    line_iter = iter(f)
    card_pubkey = int(next(line_iter).strip())
    door_pubkey = int(next(line_iter).strip())

card_loop_size = discrete_log(mod, card_pubkey, 7)
door_loop_size = discrete_log(mod, door_pubkey, 7)

print(pow(door_pubkey, card_loop_size, mod))
