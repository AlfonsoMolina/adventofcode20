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

count = sum(len(set(group.replace('\n',''))) for group in input_data)

print(count)