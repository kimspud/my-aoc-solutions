#day 6
import string

groups = []

with open("day_6_input.txt", "r") as data:
    input = data.read()

groups = input.replace('\n', ' ')
groups = list(groups.split('  '))

# part_1
def answered_once_per_group(groups):
    count_total = 0
    for group in groups:
        answers = list(group.replace(' ', ""))
        no_dups = []
        count = 0
        #print(answers)
        for answer in answers:
            if answer not in no_dups: 
                no_dups.append(answer)
        count = len(no_dups)
        count_total = count_total + count
    return count_total

# part_2
def answered_all_in_group(groups):
    count_total = 0
    alphabet =  list(string.ascii_lowercase)
    for group in groups:
        user_answers = group.split(' ')
        for char in alphabet:
            count = 0
            for answer in user_answers:
                if char in answer:
                    count = count + 1
            if count == len(user_answers):
                count_total = count_total + 1
        #print("user_answers " + str(user_answers))
        #print("---")
    return(count_total)

print("part_1: " + str(answered_once_per_group(groups))) 
print("part_2: " + str(answered_all_in_group(groups)))