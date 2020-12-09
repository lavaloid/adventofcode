import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
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

_pc = 0
_acc = 0

history = []

while code[_pc]['count'] < 1:
    history.append(_pc)
    code[_pc]['count'] += 1

    if code[_pc]['ins'] == 'acc':
        _acc += code[_pc]['arg']
        _pc += 1
    elif code[_pc]['ins'] == 'jmp':
        _pc += code[_pc]['arg']
    elif code[_pc]['ins'] == 'nop':
        _pc += 1

# If an instruction is run the second time, then it will never terminate.
# The code above will give a history of everything that happens before it loops.

def reset():
    for c in code:
        c['count'] = 0

reset()

def run():
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

        if pc >= len(code):
            reset()
            return {'pc': pc, 'acc': acc, 'success': True}
    
    reset()
    return {'pc': pc, 'acc': acc, 'success': False}

# Try out each line in 'history' to see if any of them make it terminate
for n in history:
    if code[n]['ins'] == 'acc':
        continue

    if code[n]['ins'] == 'jmp':
        code[n]['ins'] = 'nop'
    else:
        code[n]['ins'] = 'jmp'

    result = run()

    if result['success']:
        print(result['acc'])
        break
    else:
        if code[n]['ins'] == 'jmp':
            code[n]['ins'] = 'nop'
        else:
            code[n]['ins'] = 'jmp'

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
