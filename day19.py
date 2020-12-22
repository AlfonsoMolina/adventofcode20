import re

input_data = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

with open('adventofcode20/day19_input.txt', 'r') as f:    
    input_data = f.read()

rules, messages = input_data.split('\n\n')

rules = {r[0]: r[1] for rule in rules.split('\n') if (r := rule.split(': '))}
messages = [m for m in messages.split('\n')]

# Too much recursion...
def translate_rule(rule):
    new = ''
    if '|' in rule:
        one, two = rule.split('|')
        new = '(' + translate_rule(one) + '|' + translate_rule(two) + ')'
        return new
    for n in rule:
        if n in rules:
            new += translate_rule(rules[n])
        elif n:
            new += n.strip(' "')
    return new

# Look up for rules with letters...
resolved_rules = [r for r, v in rules.items() if v.strip(' "').isalpha()]

print(resolved_rules)
for r in resolved_rules:
    rules[r] = rules[r].strip(' "')
while len(resolved_rules) != len(rules):
    for r,v in rules.items():
        for i in resolved_rules:
            if i in v.split(' '):
                rr = ' ' + rules[r] + ' '
                ii = ' ' + i + ' '
                if '|' in rules[i] :
                    rules[r] = rr.replace(ii, ' (' + rules[i] + ') ')
                else:
                    rules[r] = rr.replace(ii, ' ' + rules[i] + ' ')
        if r not in resolved_rules and not any(n in v for n in '123456789'):
            resolved_rules.append(r)

main_rule = '^'  + rules['0'].replace(' ','') + '$'

res = sum(1 for m in messages if re.match(main_rule,m))

print(res)