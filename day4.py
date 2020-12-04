def is_valid(passport):
    try:
        hgt_units = passport["hgt"][-2:]
        hgt_val = int(passport["hgt"][:-2])
        int(passport["pid"])
    except:
        return False
    return (
        1920 <= int(passport["byr"]) <= 2002
        and 2010 <= int(passport["iyr"]) <= 2020
        and 2020 <= int(passport["eyr"]) <= 2030
        and (
            (hgt_units == "cm" and 150 <= hgt_val <= 193)
            or (hgt_units == "in" and 59 <= hgt_val <= 76)
        )
        and len(passport["hcl"]) == 7
        and passport["hcl"][0] == "#"
        and all(i in "1234567890abcdef" for i in passport["hcl"][1:])
        and passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        and len(passport["pid"]) == 9
    )

passports = []
passport = {}
with open("day4.in") as f:
    for line in f:
        if not line.strip():
            passports.append(passport)
            passport = {}
        else:
            for pair in line.split(' '):
                key, value = pair.split(':')
                passport[key.strip()] = value.strip()
passports.append(passport)
print(len(passports))
required_fields = (
    "byr",
    "eyr",
    "iyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
)
count = 0
for passport in passports:
    if all(i in passport.keys() for i in required_fields):
        count += 1
        print("yes", end=" ")
    else:
        print("no", end="  ")
    for key in sorted(passport.keys()):
        print(key, end=" ")
    print()
print("part 1:", count)

# part 2

count = 0
for passport in passports:
    if all(i in passport.keys() for i in required_fields):
        if is_valid(passport):
            count += 1
print("part 2:", count)
