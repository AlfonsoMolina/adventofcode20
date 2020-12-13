from itertools import count
input_data = """2,x,3,5
7,13,x,x,59,x,31,19
17,x,13,19
67,7,59,61
67,x,7,59,61
67,7,x,59,61
1789,37,47,1889"""

input_data = [line for line in input_data.split('\n')]

input_data = ['13,x,x,41,x,x,x,x,x,x,x,x,x,997,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,619,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17']

# See: Chinese remainder theorem

for line in input_data:
    print(line)
    buses = {int(bus):int(bus)-i for i, bus in enumerate(line.split(',')) if bus != 'x'}
    buses_ordered = sorted([bus for bus in buses], reverse = True)

    mcm = buses_ordered[0]
    offset = buses[mcm]
    # Add busses one by one, and increase the steps each time
    for bus in buses_ordered[1:]:
        for timestamp in count(start = offset, step = mcm):
            if (timestamp - buses[bus]) % bus == 0:
                break
        offset = timestamp
        mcm *= bus
    
    print(offset)