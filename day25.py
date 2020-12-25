from itertools import count
from sympy.ntheory.residue_ntheory import discrete_log

mod = 20201227

def transform(number, loop_size):
    return pow(number, loop_size, mod)

with open("day25.in") as f:
    line_iter = iter(f)
    card_pubkey = int(next(line_iter).strip())
    door_pubkey = int(next(line_iter).strip())

card_loop_size = discrete_log(mod, card_pubkey, 7)
print(card_loop_size)

door_loop_size = discrete_log(mod, door_pubkey, 7)
print(door_loop_size)

print(transform(door_pubkey, card_loop_size))
print(transform(card_pubkey, door_loop_size))
