import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
input_str = f.read().split("\n")

# Fun logic
def traverse(dx, dy):
    count = 0

    x = 0
    y = 0
    WIDTH = len(input_str[0])
    HEIGHT = len(input_str) - 1

    while y < HEIGHT:
        check = input_str[y][x]
        if check == '#':
            count += 1

        x += dx
        if x >= WIDTH:
            x -= WIDTH
        y += dy
    
    print(count)
    return count

a = traverse(1, 1)
b = traverse(3, 1)
c = traverse(5, 1)
d = traverse(7, 1)
e = traverse(1, 2)

print(a * b * c * d * e)

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
