input_data = """19,0,5,1,10,13"""

numbers = [int(i) for i in input_data.split(',')]
log = {}

# Initial phase
for turn in range(1, len(numbers)+1):
    spoken = numbers[turn -1]
    if spoken not in log:
        log[spoken] = [turn]
    else:
        log[spoken].append(turn)

for turn in range(len(numbers)+1, 30000001):
    if turn % 10000 == 0:
        print(turn)
    if len(log[spoken]) == 1:
        spoken = 0
    else:
        spoken = log[spoken][-1] - log[spoken][-2]
        
    if spoken in log:
        log[spoken].append(turn)
        # Free memory
        if len(log[spoken]) > 2:
            log[spoken].pop(0)
    else:
        log[spoken] = [turn]
    
print(spoken)