from functools import reduce
from math import sqrt

input_data = """389125467"""
input_data = '362981754'

# with open('adventofcode20/day22_input.txt', 'r') as f:    
#     input_data = f.read()

cups = [int(c) for c in input_data]
length = len(cups)
current_cup = cups[-1]
for i in range(100):
    print(f'-- move {i} --')
    print('cups', cups)
    current_index = (cups.index(current_cup) + 1) %length
    current_cup = cups[current_index]
    print('current', current_cup)
    start_slice = (current_index + 1) % length
    stop_slice = (current_index + 4) % length
    if stop_slice > start_slice:
        pick_up = cups[start_slice:stop_slice]
        print(pick_up)
        cups = cups[:start_slice] + cups[stop_slice:]
    else:
        pick_up = cups[start_slice:] + cups[:stop_slice]
        print(pick_up)
        cups = cups[stop_slice:start_slice]
    destination = (current_cup - 1) % length
    # If it is a zero, change it for the max value
    destination = destination if destination else length
    while True:
        if destination in cups:
            break
        else:
            destination = (destination - 1) % length
            destination = destination if destination else length
    print('destination', destination)
    index = cups.index(destination)
    cups = cups[:index+1] + pick_up + cups[index+1:]

start = cups.index(1)
res = cups[start+1:] + cups[:start]
print(''.join(str(i) for i in res))