import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
input_str = f.read().split('\n')

# Fun logic
data = [0] * 26
count = 0
group_member_no = 0

for line in input_str:
    if line == '':
        for i in range(26):
            if data[i] == group_member_no:
                count += 1
            data[i] = 0
        group_member_no = 0
        continue

    group_member_no += 1
    for ch in line:
        data[ord(ch) - ord('a')] += 1

print(count)

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
