import string

groups = []
count_total = 0
alphabet =  list(string.ascii_lowercase)

with open("day_6_input.txt", "r") as data:
    input = data.read()
    groups = input.replace('\n', ' ')
print(groups)
groups = list(groups.split('  '))
print(groups)

for group in groups:
    user_answers = group.split(' ')
    for char in alphabet:
        count = 0
        for answer in user_answers:
            if char in answer:
                count = count + 1
        if count == len(user_answers):
            count_total = count_total + 1
    print("user_answers " + str(user_answers))
    print("---")
print(count_total)
    


    


