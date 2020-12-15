# day 15
numbers = []
last_number = 0

# read input file and make list from input
with open("day_15_input.txt", "r") as input:
    for line in input:
        input = line.split(",")
        numbers = list(map(int, input))

while len(numbers) < 2021:
    print(f"numbers: {numbers}")
    # Is the last number new?
    #If yes, add 0
    if numbers.count(numbers[-1]) == 1:
        numbers.append(0)
    #If no, when was the number last used? index of now - last used.
    else:
        last_number = numbers[-1]
        #print(f"last_number: {last_number}")
        temp = []
        for i in range( len(numbers) - 1, -1, -1) :
            #print(numbers[i])
            if numbers[i] == last_number:
                #print(f"I match: {i}")
                temp.append(i)
                #print(f"temp: {temp}")
        numbers.append(temp[0] - temp[1])

print(f"final: {numbers[2019]}")