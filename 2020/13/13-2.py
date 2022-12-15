import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
input_str = f.read().split('\n')

# Fun logic
buses = []
i = -1
for str_bus in input_str[1].split(','):
    i += 1
    if str_bus == 'x':
        continue
    buses.append({'bus': int(str_bus), 'offset': i})

jump = buses[0]['bus']
count = 0
next_bus = 1
BUS_TOTAL = len(buses)
while next_bus < BUS_TOTAL:
    count += jump
    check_bus = buses[next_bus]['bus']
    check_offset = buses[next_bus]['offset'] % check_bus
    offset = check_bus - count % check_bus
    if check_offset == offset:
        # If we want to be technically correct, jump should
        # be changed to the LCM of current jump and next bus
        # ID, but since everything is primes we don't need to
        # do that
        jump *= check_bus
        next_bus += 1

print(count)

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
