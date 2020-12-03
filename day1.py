lines = []
with open("day1.in") as f:
    lines = [int(i.strip()) for i in f.readlines()]

for num1 in lines:
    for num2 in lines:
        if num1 + num2 == 2020:
            print(num1 * num2)
            break

for num1 in lines:
    for num2 in lines:
        for num3 in lines:
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)