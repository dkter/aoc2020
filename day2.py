from collections import namedtuple

Password = namedtuple('Password', ['lower_bound', 'upper_bound', 'required_letter', 'password'])

passwords = []
with open("day2.in") as f:
    for line in f:
        req, password = line.split(':')
        bounds, letter = req.split(' ')
        lower_bound, upper_bound = bounds.split('-')
        passwords.append(Password(int(lower_bound), int(upper_bound), letter, password))

count = 0
for password in passwords:
    if password.lower_bound <= password.password.count(password.required_letter) <= password.upper_bound:
        count += 1

print(count)

count2 = 0
for password in passwords:
    if (password.password[password.lower_bound] == password.required_letter, password.password[password.upper_bound] == password.required_letter).count(True) == 1:
        count2 += 1

print(count2)
