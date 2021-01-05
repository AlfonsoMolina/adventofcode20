from itertools import product
from copy import deepcopy
input_data = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

# with open('adventofcode20/day16_input.txt', 'r') as f:    
#     input_data = f.read()

my_ticket = []
tickets = []
rules = {}
scanning_error = 0
fields = []

# Read input
step = 0
for line in input_data.split('\n'):
    if "your ticket" in line:
        step = 1
    elif "nearby tickets" in line:
        step = 2
    elif not line:
        continue
    else:
        if step == 0:
            field = line.split(':')[0]
            field_rules = line.split(':')[1].split(' or ')
            rules[field] = []
            for r in field_rules:
                rules[field].append([int(n) for n in r.split('-')])
            fields.append(field)
        elif step == 1:
            my_ticket = [int(n) for n in line.split(',')]
        elif step == 2:
            tickets.append([int(n) for n in line.split(',')])

for t in tickets[:]:
    for field in t:
        for r in rules.values():
            # Check if field f is valid for the rule r
            if r[0][0] <= field <= r[0][1] or r[1][0] <= field <= r[1][1]:
                break
        else:
            scanning_error += field

print(scanning_error)