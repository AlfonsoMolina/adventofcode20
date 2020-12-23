from functools import reduce
from math import sqrt

input_data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

with open('adventofcode20/day21_input.txt', 'r') as f:    
    input_data = f.read()

input_data = input_data.split('\n')

alergen_list = []
ingredient_list = []
candidates_list = {}
for line in input_data:
    ingredients = line.split('(')[0].split()
    alergens = line.split('(')[1][:-1]
    alergens = alergens.replace('contains ', '').split(', ')
    alergen_list.extend(alergens)
    ingredient_list.extend(ingredients)
    for alergen in alergens:
        if alergen in candidates_list:
            new = set(ingredients)
            candidates_list[alergen] = new & candidates_list[alergen]
        else:
            candidates_list[alergen] = set(ingredients)
ingredient_list = set(ingredient_list)
alergen_list = set(alergen_list)
# Reduce candidates
while any(len(candidates_list[c]) > 1 for c in candidates_list):
    for c in candidates_list:
        if len(candidates_list[c]) == 1:
            target = list(candidates_list[c])[0]
            for cc in candidates_list:
                if c != cc and target in candidates_list[cc]:
                    candidates_list[cc].remove(target)

# safe food
safe = [i for i in ingredient_list if not any(i in candidates_list[c] for c in candidates_list)]

# Now count...
counter = {}
for ingredient in safe:
    counter[ingredient] = 0
    for line in input_data:
        if ingredient in line:
            counter[ingredient] += 1

alergen_list = {list(v)[0]:k for k,v in candidates_list.items()}
unsafe = ingredient_list - set(safe)
res = ','.join(sorted(list(unsafe), key=lambda x: alergen_list[x]))
print(res)