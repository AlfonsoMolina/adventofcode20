input_data = """abc

a
b
c

ab
ac

a
a
a
a

b"""

with open('adventofcode20/day06_input.txt', 'r') as f:    
    input_data = f.read()

input_data = input_data.split('\n\n')

count = 0
for group in input_data:
    people = [set(person) for person in group.split('\n')]
    count += len(set.intersection(*people))

print(count)