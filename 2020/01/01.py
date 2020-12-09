import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
input_str = f.read().split()

nums = []
for s in input_str:
    nums.append(int(s))

nums.sort()

# Fun logic
length = len(nums)
TARGET = 2020

found = False

for i in range(length):
    need = TARGET - nums[i]

    # Binary search!!!!!!!
    l = i + 1
    r = length - 1
    while l <= r:
        mid = (l + r) // 2

        if (nums[mid] == need):
            found = True
            break
        elif nums[mid] < need:
            l = mid + 1
        elif nums[mid] > need:
            r = mid - 1

    if found:
        print(f"{nums[i] * need}")
        break

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
