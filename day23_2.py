input_data = "389125467"
input_data = '362981754'
length = 1000000

input_data = [int(c) for c in input_data] + [c for c in range(10, length+1)]

# Create the dictionary
ring = {}
for i in range(length):
    cup = input_data[i]
    prev_cup = input_data[(i - 1) % length]
    next_cup = input_data[(i + 1) % length]

    ring[cup] = {'prev': prev_cup, 'next': next_cup}


current_cup = int(input_data[0])
for i in range(10000000):
    if i % 1000000 == 0:
        print(i)
    # Pick up the three next cups
    # It could be prettier, I know.
    pick_up = []
    n = ring[current_cup]['next']
    nn = ring[n]['next']
    nnn = ring[nn]['next']
    
    pick_up = [n, nn, nnn]

    # Remove them from the ring
    ring[current_cup]['next'] = ring[nnn]['next'] 
    ring[ring[nnn]['next']]['prev'] = current_cup
    
    destination = (current_cup - 1) % length
    destination = destination if destination else length
    while destination in pick_up:
        destination = (destination - 1) % length
        destination = destination if destination else length

    # Put them after destination...
    end = ring[destination]['next']
    ring[destination]['next'] = n
    ring[n] = {'prev': destination, 'next': nn}
    ring[nn] = {'prev': destination, 'next': nnn}
    ring[nnn] = {'prev': destination, 'next': end}

    current_cup = ring[current_cup]['next']


res = ring[1]['next'] * ring[ring[1]['next']]['next']

