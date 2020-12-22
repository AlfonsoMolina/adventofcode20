import re

input_data = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""

with open('adventofcode20/day19_input.txt', 'r') as f:    
    input_data = f.read()

rules, messages = input_data.split('\n\n')

rules = {r[0]: r[1] for rule in rules.split('\n') if (r := rule.split(': '))}
messages = [m for m in messages.split('\n')]

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

# Update rules
rules['8'] = '( 42 )+'
rules['11'] = '((?P<one> 42 +)(?P<two> 31 +))' 
rules['11'] = '( 42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 | 42 42 42 42 42 42 31 31 31 31 31 31 )' 

#rule = '^' + translate_rule(rules['0']) + '$'
# Look up for rules with letters...
resolved_rules = [r for r, v in rules.items() if v.strip(' "').isalpha()]

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

    # Fast skipç
    if not any(n in rules['0'] for n in '123456789'):
        break
main_rule = '^'  + rules['0'].replace(' ','') + '$'

count = 0

for m in messages:
    if r := re.match(main_rule, m):
        count += 1

print(count)