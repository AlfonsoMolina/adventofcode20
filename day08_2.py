import copy
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

source_code = {}
for i, x in enumerate(input_data.split('\n')):
    op = x.split()[0]
    arg = int(x.split()[1])
    source_code[i] = {'op':op, 'arg':arg}
    

changed_line = 0
while changed_line < len(source_code):
    code = copy.deepcopy(source_code)
    if code[changed_line]['op'] == 'nop':
        code[changed_line]['op'] = 'jmp'
    elif code[changed_line]['op'] == 'jmp':
        code[changed_line]['op'] = 'nop'
    else:
        changed_line += 1
        continue

    instruction = 0
    accumulator = 0

    while instruction < len(code):
        if 'executed' in code[instruction]:
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
    else:
        print('Program exited normally.')
        print('Wrong line: ', changed_line)
        print(accumulator)
        break

    changed_line += 1