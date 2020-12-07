input_data = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

with open('adventofcode20/day07_input.txt', 'r') as f:    
    input_data = f.read()

input_data = input_data.split('\n')
rules = {}

# Add rule: {'red bag': {'white bag':1, 'yellow bag': 2}}
def read_line(rules, line):
    master = line.split(' contain ')[0]
    if master[-1] == 's':
        master = master[:-1]
    slaves = line.split(' contain ')[1].split(', ')
    rule = {}
    for slave in slaves:
        if slave == 'no other bags.':
            continue
        number = int(slave.split()[0])
        bag = " ".join(slave.split()[1:])
        if bag[-1] == '.':
            bag = bag[:-1]
        if bag[-1] == 's':
            bag = bag[:-1]
        rule[bag] = number
    rules[master] = rule

def get_bag_count(bag):
    if not rules[bag]:
        return 1
    count = 1
    for subbag, number in rules[bag].items():
        count += number * get_bag_count(subbag)
    return count

for line in input_data:
    read_line(rules, line)

target = 'shiny gold bag'
c = get_bag_count(target)
print(c-1)
