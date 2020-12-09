import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
input_str = f.read().split('\n')

# Fun logic
data = [False] * 26
count = 0

for line in input_str:
    if line == '':
        for i in range(26):
            if data[i]:
                count += 1
            data[i] = False
        continue

    for ch in line:
        data[ord(ch) - ord('a')] = True

print(count)

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
