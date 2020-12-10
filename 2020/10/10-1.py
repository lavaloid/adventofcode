import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
input_str = f.read().split('\n')
input_str.pop()

# Fun logic
nums = []
for line in input_str:
    nums.append(int(line))

nums.sort()

one_diff = 0
three_diff = 0
for i in range(len(nums) - 1):
    if (nums[i + 1] - nums[i] == 1):
        one_diff += 1
    if (nums[i + 1] - nums[i] == 3):
        three_diff += 1

if nums[0] == 1:
    one_diff += 1
if nums[0] == 3:
    three_diff += 1

three_diff += 1

print(f"{one_diff} {three_diff} {one_diff * three_diff}")

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
