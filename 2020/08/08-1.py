import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("08.txt", "r")
input_str = f.read().split('\n')
input_str.pop()

# Fun logic
code = []

for line in input_str:
    instruction = line[:3]
    argument = line[4:]

    code.append({
        'ins': instruction,
        'arg': int(argument),
        'count': 0
    })

pc = 0
acc = 0

while code[pc]['count'] < 1:
    code[pc]['count'] += 1

    if code[pc]['ins'] == 'acc':
        acc += code[pc]['arg']
        pc += 1
    elif code[pc]['ins'] == 'jmp':
        pc += code[pc]['arg']
    elif code[pc]['ins'] == 'nop':
        pc += 1

print(acc)

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
