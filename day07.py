input_data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

with open('adventofcode20/day07_input.txt', 'r') as f:    
    input_data = f.read()

input_data = input_data.split('\n')

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

def get_inverse_rules(rules):
    rules_inv = {}
    for bag, subbags in rules.items():
        for subbag in subbags:
            if subbag not in rules_inv:
                rules_inv[subbag] = [bag]
            else:
                rules_inv[subbag].append(bag)
    return rules_inv
    
rules = {}

for line in input_data:
    read_line(rules, line)

rules_inv = get_inverse_rules(rules)

target = 'shiny gold bag'
options = rules_inv[target]
new_options = rules_inv[target]

while new_options:
    new = new_options[:]
    new_options = []
    for bag in new:
        if bag not in rules_inv:
            continue
        for superbag in rules_inv[bag]:
            if superbag not in options:
                options.append(superbag)
                new_options.append(superbag)

print(options)
print(len(set(options)))
