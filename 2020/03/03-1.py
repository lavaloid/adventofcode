import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("03.txt", "r")
input_str = f.read().split("\n")

# Fun logic
count = 0

x = 0
y = 0
WIDTH = len(input_str[0])
HEIGHT = len(input_str) - 1

while y < HEIGHT:
    check = input_str[y][x]
    if check == '#':
        count += 1

    x += 3
    if x >= WIDTH:
        x -= WIDTH
    y += 1

print(count)

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
