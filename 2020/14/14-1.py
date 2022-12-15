import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
input_str = f.read().split('\n')

# Fun logic
buses = []
for str_bus in input_str[1].split(','):
    if str_bus == 'x':
        continue
    buses.append(int(str_bus))

start = int(input_str[0])
min_bus = 0
min_wait = -1

for bus in buses:
    last_depart = start % bus
    wait = bus - last_depart
    if min_wait == -1:
        min_wait = wait
    else:
        if wait < min_wait:
            min_bus = bus
            min_wait = wait

print(min_bus * min_wait)

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
