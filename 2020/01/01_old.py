import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("01.txt", "r")
input_str = f.read().split()

nums = []
for s in input_str:
    nums.append(int(s))

found = False

for i in nums:
    for j in nums:
        if i + j == 2020: 
            print(i * j)
            found = True
            break
    if found:
        break

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
