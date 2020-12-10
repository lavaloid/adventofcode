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

last = len(nums) - 1
device_jolt = nums[last] + 3
count = 0

result = [0] * len(nums)

result[last] = 1

# For device with joltage J, the number of possibilities must equal to
# the sum of the possibilities of whichever of J+1, J+2, and J+3 exists.

result[last - 1] = result[last]
result[last - 2] = result[last - 1]
if result[last] - result[last - 2] <= 3:
    result[last - 2] += result[last]

for i in range(last-3, -1, -1):
    result[i] += result[i + 1]
    if nums[i + 2] - nums[i] <= 3:
        result[i] += result[i + 2]
    if nums[i + 3] - nums[i] <= 3:
        result[i] += result[i + 3]

print(result[0] + result[1] + result[2])

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
