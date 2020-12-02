#day 2

def old_policy_valid_count():
    valid_count = 0
    with open("day2_input.txt", "r") as input:
        for line in input:
            password_list = list(line.split(" "))
            range = list(password_list[0].split("-"))
            letter = password_list[1].replace(":", "")
            password = password_list[2]
            if int(range[0]) <= password.count(letter) <= int(range[1]):
                valid_count = valid_count + 1
        return valid_count

def new_policy_valid_count():
    valid_count = 0
    with open("day2_input.txt", "r") as input:
        for line in input:
            password_list = list(line.split(" "))
            range = list(password_list[0].split("-"))
            letter = password_list[1].replace(":", "")
            password = list(password_list[2])
            rule_1 = int(range[0]) - 1
            rule_2 = int(range[1]) - 1
            if password[rule_1] == letter and password[rule_2] != letter or password[rule_1] != letter and password[rule_2] == letter:
               valid_count = valid_count + 1
        return valid_count

old_policy_valid_count()
new_policy_valid_count()
