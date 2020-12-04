input_data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

with open('adventofcode20/day04_input.txt', 'r') as f:    
    input_data = f.read()

input_data = input_data.split('\n')

fields = "byr iyr eyr hgt hcl ecl pid cid".split()

def read_passports():
    passports = []
    pp = {}
    for line in input_data:
        if not line:
            passports.append(pp)
            pp = {}
        for data in line.split():
            f, v = data.split(':')
            pp[f] = v
    passports.append(pp)
    return passports

def validate_passport(passport, fields):
    return all(field in passport for field in fields)

passports = read_passports()

valid_passports = 0
fields.remove('cid')

for p in passports:
    valid_passports += 1 if validate_passport(p, fields) else 0

print(valid_passports)