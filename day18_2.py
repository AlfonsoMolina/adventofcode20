input_data = """1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""

with open('adventofcode20/day18_input.txt', 'r') as f:    
    input_data = f.read()

input_data = [line for line in input_data.split('\n')]

def evaluate (line): 
    line = line.split()
    # First +
    while '+' in line:
        i = line.index('+')
        res = int(line[i-1]) + int(line[i+1])
        line = line[:i-1] + [str(res)] + line[i+2:]
    while '*' in line:
        i = line.index('*')
        res = int(line[i-1]) * int(line[i+1])
        line = line[:i-1] + [str(res)] + line[i+2:]

    return int(line[0])

sum_res = 0

for line in input_data:
    # Change parenthesis
    while ')' in line:
        end = [i for i, x in enumerate(line) if x == ")"][0]
        start = [i for i, x in enumerate(line[:end]) if x == "("][-1]
        section = line[start+1:end]
        res = evaluate(section)
        line = line[:start] + str(res) + line[end+1:]
    res = evaluate(line)
    
    res = evaluate(line)
    sum_res += res

print(sum_res)