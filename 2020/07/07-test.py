f = open("07.txt", "r")
input_str = f.read().split('\n')
input_str.pop()

print(len(input_str))

hashes = []
for line in input_str:
    hash = 0
    line_split = line.split()
    str = line_split[0] + ' ' + line_split[1]
    for i in range(len(str)):
        hash += ord(str[i]) * (i + 1)
    if hash not in hashes:
        hashes.append(hash)

print(len(hashes))
