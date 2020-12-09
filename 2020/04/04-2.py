import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")

import re
input_str = re.split('\n| ', f.read())

# Fun logic
count = 0

data = {
    'byr': None,
    'iyr': None,
    'eyr': None,
    'hgt': None,
    'hcl': None,
    'ecl': None,
    'pid': None
}

def valid():
    # Check if anything is empty first
    for key in data:
        if data[key] == None:
            return False

    # byr
    if not (1920 <= int(data['byr']) <= 2002):
        return False

    # iyr
    if not (2010 <= int(data['iyr']) <= 2020):
        return False

    # eyr
    if not (2020 <= int(data['eyr']) <= 2030):
        return False

    # hgt
    if len(data['hgt']) < 3:
        return False
    suf = data['hgt'][-2:] # last 2 chars
    hgt = int(data['hgt'][:-2]) # everything but the last 2 chars
    if suf == 'cm':
        if not (150 <= hgt <= 193):
            return False
    elif suf == 'in':
        if not (59 <= hgt <= 76):
            return False
    else:
        return False

    # hcl
    if data['hcl'][0] != '#':
        return False
    if len(data['hcl']) != 7:
        return False
    for ch in data['hcl'][1:]:
        if not (ord('0') <= ord(ch) <= ord('9') or ord('a') <= ord(ch) <= ord('f')):
            return False

    # ecl
    valid_ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    ecl_is_valid = False
    for col in valid_ecl_list:
        if data['ecl'] == col:
            ecl_is_valid = True
            break
    if not ecl_is_valid:
        return False

    # pid
    if len(data['pid']) != 9:
        return False
    for ch in data['pid']:
        if not (ord('0') <= ord(ch) <= ord('9')):
            return False

    return True

def reset():
    for key in data:
        data[key] = None

for element in input_str:
    if element == "":
        if valid():
            count += 1
        reset()
        continue

    for key in data:
        if element[:3] == key:
            data[key] = element[4:]
            break

print(count)

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
