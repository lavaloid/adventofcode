import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("05.txt", "r")
input_str = f.read().split('\n')

# Fun logic
POWER_OF_TWO = [1, 2, 4, 8, 16, 32, 64, 128]

max_id = 0

for seat in input_str:
    if len(seat) == 0:
        continue

    row = 0
    col = 0

    # row
    for i in range(7):
        if seat[i] == 'B':
            row += POWER_OF_TWO[6 - i]

    # column
    for i in range(3):
        if seat[i + 7] == 'R':
            col += POWER_OF_TWO[2 - i]

    seat_id = row * 8 + col
    if seat_id > max_id:
        max_id = seat_id

print(max_id)

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
