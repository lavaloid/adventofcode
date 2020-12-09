import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
input_str = f.read().split('\n')
input_str.pop()

# Fun logic
num = []
for line in input_str:
    num.append(int(line))

def valid(idx):
    if (idx < 25): return True

    for i in range(idx - 25, idx):
        for j in range(i + 1, idx):
            if num[i] + num[j] == num[idx]:
                return True

    return False

ptr = 0
while valid(ptr):
    ptr += 1

print(num[ptr])

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
