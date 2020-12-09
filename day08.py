input_data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

with open('adventofcode20/day08_input.txt', 'r') as f:    
    input_data = f.read()

code = {}
for i, x in enumerate(input_data.split('\n')):
    op = x.split()[0]
    arg = int(x.split()[1])
    code[i] = {'op':op, 'arg':arg}
    
instruction = 0
accumulator = 0

while True:
    if 'executed' in code[instruction]:
        print(accumulator)
        break
    else:
        code[instruction]['executed'] = True
    op = code[instruction]['op']
    arg = code[instruction]['arg']
    if op == 'acc':
        accumulator += arg
        instruction += 1
    elif op == 'jmp':
        instruction += arg
    elif op == 'nop':
        instruction += 1
        