input_data = """939
7,13,x,x,59,x,31,19"""

with open('adventofcode20/day13_input.txt', 'r') as f:    
    input_data = f.read()

input_data = [line for line in input_data.split('\n')]

departure = int(input_data[0])
buses = [int(bus) for bus in input_data[1].split(',') if bus != 'x']
print(buses)
wait_times = [bus - departure % bus  for bus in buses]

print(wait_times)
print(buses[wait_times.index(min(wait_times))]*min(wait_times))