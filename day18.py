input_data = """2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""


with open('adventofcode20/day18_input.txt', 'r') as f:    
    input_data = f.read()

input_data = [line for line in input_data.split('\n')]

def evaluate (line): 
    res = None
    op = None
    #print(line.strip())
    for n in line.strip().split(' '):
        if n == ' ':
            continue
        elif n == '+':
            op = n
        elif n == '*':
            op = n
        elif n.isnumeric():
            if res is None:
                res = int(n) 
            else:
                if op == '+':
                    res += int(n)
                elif op == '*':
                    res *= int(n)
    return res

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
    
    sum_res += res

print(sum_res)