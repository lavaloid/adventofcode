import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
input_str = f.read().split('\n')
input_str.pop()

# Fun logic
COLOR_COUNT = len(input_str)
count = 0

# IMPORTANT: This solution needs `networkx` library!!!!!!!
# Install with `pip install networkx`
import networkx as nx
from bisect import bisect_left

bags = nx.DiGraph()

# Convert colors into IDs, sorted alphabetically. 
bags_list = []
for line in input_str:
    line_split = line.split()
    bags_list.append(line_split[0] + ' ' + line_split[1])
bags_list.sort()

shiny_gold = bisect_left(bags_list, 'shiny gold')

# Create a (directed) graph `bags`.
# A -[n]-> B means "B can contain n A-bags".
# This makes it easy to find all nodes that contain "shiny gold".
for line in input_str:
    line_split = line.split()
    new_bag = bisect_left(bags_list, line_split[0] + ' ' + line_split[1])
    for i in range(1, len(line_split)//4):
        contains = bisect_left(bags_list, line_split[4 * i + 1] + ' ' + line_split[4 * i + 2])
        bags.add_edge(contains, new_bag, amount = int(line_split[4 * i]))

can_contain_shiny_gold = nx.descendants(bags, shiny_gold)

print(len(can_contain_shiny_gold))

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
