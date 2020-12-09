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

key = num[ptr]

left_ptr = 0
right_ptr = 0
current_sum = num[0]
while current_sum != key:
    while current_sum < key:
        right_ptr += 1
        current_sum += num[right_ptr]
    
    while current_sum > key:
        left_ptr += 1
        current_sum -= num[left_ptr - 1]

min_number = float('inf')
max_number = 0
for i in range(left_ptr, right_ptr + 1):
    if num[i] < min_number: min_number = num[i]
    if num[i] > max_number: max_number = num[i]

print(min_number + max_number)

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
