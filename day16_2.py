from itertools import product
from copy import deepcopy
input_data = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

with open('adventofcode20/day16_input.txt', 'r') as f:    
    input_data = f.read()

my_ticket = []
my_ticket_fields = {}
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
            tickets.remove(t)

possible_columns = {}
for field, rule in rules.items():
    possible_columns[field] = []
    # Check one by on to find the position
    for i in range(len(my_ticket)):
        for ticket in tickets:
            if not (rule[0][0] <= ticket[i] <= rule[0][1] 
                or rule[1][0] <= ticket[i] <= rule[1][1]):
                break
        else:
            # print(i, field, rule, my_ticket[i])
            # my_ticket_fields[field] = my_ticket[i]
            # break
            possible_columns[field].append(i)

while any(len(f) > 1 for f in possible_columns.values()):
    # All fields have all previous fields plus one. Check the longest one and
    # we must find a field that cannot be anything else.
    options = [value for value in possible_columns.values() if len(value) > 1]
    options.sort(key=len, reverse=True)
    
    for field_position in options[0]:
        possible_fields = []
        for field, values in possible_columns.items():
            if field_position in values:
                possible_fields.append(field)
        if len(possible_fields) == 1:
            possible_columns[possible_fields[0]] = [field_position]
            my_ticket_fields[possible_fields[0]] = my_ticket[field_position]
            break
    else:
        break

print(possible_columns)
print(my_ticket_fields)

result = 1
for field, value in my_ticket_fields.items():
    if field.startswith('departure'):
        result *= value
print(result)