import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
input_str = f.read().split("\n")

# Fun logic
count = 0

for s in input_str:
    i = 0
    min_str = ""
    if len(s) == 0: 
        continue
    while s[i] != "-":
        min_str += s[i]
        i += 1

    i += 1
    max_str = ""
    while s[i] != " ":
        max_str += s[i]
        i += 1

    i += 1
    find_char = s[i]

    min_num = int(min_str)
    max_num = int(max_str)

    i += 3
    length = len(s)
    
    if (s[i + max_num - 1] == find_char) ^ (s[i + min_num - 1] == find_char):
        count += 1

print(count)

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
