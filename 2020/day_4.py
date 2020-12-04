#day_4 - part2

import re
input = ""
passports = []
valid_count = 0
invalid_count = 0

def validate_fields(info):
    fields = {}
    is_valid = []

    for item in info:
        key, val = item.split(":")
        fields[key] = val

    for k in fields:
        if k == "byr" and len(fields[k]) == 4 and 1920 <= int(fields[k]) <= 2002:
            is_valid.append(True)
        elif k == "iyr" and len(fields[k]) == 4 and 2002 <= int(fields[k]) <= 2020:
            is_valid.append(True)
        elif k == "eyr" and len(fields[k]) == 4 and 2020 <= int(fields[k]) <= 2030:
            is_valid.append(True)
        elif k == "hgt":
            height = fields[k]
            if "cm" in height:
                height_number = height[ 0 : 3 ]
                if height_number.isnumeric() and 150 <= int(height_number) <= 193:
                    is_valid.append(True)
            if "in" in height:
                height_number = height [ 0 : 2]
                if height_number.isnumeric() and 59 <= int(height_number) <= 76:
                    is_valid.append(True)
        elif k == "pid" and len(fields[k]) == 9 and fields[k].isnumeric():
            is_valid.append(True)
        elif k == "ecl":
            options = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            count = 0
            for option in options:
                if fields[k] == option:
                    count = count + 1
            if count == 1:
                is_valid.append(True)
        elif k == "hcl" and fields[k].startswith("#") and len(fields[k]) == 7:
            hair_color_id = (fields[k])
            count = re.findall("[0123456789abcdef]", hair_color_id)
            if len(count) == 6:
                is_valid.append(True)
    if len(is_valid) == 7:
       return True

with open("day_4_input.txt", "r") as data:
    input = data.read()
    passports = input.replace('\n', ' ')

passports = passports.split('  ')
valid_count = 0
for passport in passports:
    info = []
    info = passport.split(' ')
    if len(info) == 8 and validate_fields(info) is True:
        valid_count = valid_count + 1
    elif len(info) == 7 and validate_fields(info) is True:
        valid_count = valid_count + 1
print(valid_count)       
         




