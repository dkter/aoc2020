lines = None
with open("day5.in") as f:
    lines = [l.strip() for l in f.readlines()]

highest_seat_id = 0
seat_ids = []
for line in lines:
    row_range = [0, 127]
    col_range = [0, 7]
    for char in line:
        if char == "F":
            row_range[1] -= (row_range[1] - row_range[0]) // 2 + 1
        elif char == "B":
            row_range[0] += (row_range[1] - row_range[0]) // 2 + 1
        elif char == "L":
            col_range[1] -= (col_range[1] - col_range[0]) // 2 + 1
        elif char == "R":
            col_range[0] += (col_range[1] - col_range[0]) // 2 + 1

    seat_id = row_range[0] * 8 + col_range[0]
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id
    seat_ids.append(seat_id)

print(highest_seat_id)

for id in range(0, highest_seat_id):
    if id not in seat_ids and id+1 in seat_ids and id-1 in seat_ids:
        print(id)
