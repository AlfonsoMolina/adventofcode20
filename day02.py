from itertools import permutations

input_data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

with open('adventofcode20/day02_input.txt', 'r') as f:    
    input_data = f.read()

input_data = input_data.split('\n')

count = 0

for row in input_data:
    psw = row.split()[-1]
    a, b = row.split()[0].split('-')
    letter = row.split()[1][0]

    if int(a) <= psw.count(letter) <= int(b):
        count+=1

print(count)
