import string

groups = []
count_total = 0

with open("day_6_input.txt", "r") as data:
    input = data.read()
    groups = input.replace('\n', ' ')

groups = list(groups.split('  '))

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
print(count_total)
    


    


