import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("04.txt", "r")

import re
input_str = re.split('\n| ', f.read())

# Fun logic
count = 0

data = {
    'byr': 0,
    'iyr': 0,
    'eyr': 0,
    'hgt': 0,
    'hcl': 0,
    'ecl': 0,
    'pid': 0
}

def valid():
    for key in data:
        if data[key] == 0:
            return False
    return True

def reset():
    for key in data:
        data[key] = 0

for element in input_str:
    if element == "":
        if valid():
            count += 1
        reset()
        continue

    for key in data:
        if element[:3] == key:
            data[key] += 1
            break

print(count)

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
