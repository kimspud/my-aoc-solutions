#day_9

numbers = []
#print(f"numbers: {numbers}")

with open("day_9_input.txt", "r") as data:
    for line in data:
        numbers.append(line.strip("\n"))

# find a number in the list that is not a sum of the designated X numbers before it
def number_not_a_sum(numbers, start, stop):
    while stop < len(numbers):
        range_list = numbers[start:stop]
        sums = []
        print(f"range_list: {range_list}")
        #starting at index 5 + 1, is the current number in the string of possible sums
        #find if 
        length = len(range_list)
        for i in range(length):
            for v in range_list:
                #print(f"v: {v}")
                #print(f"value: {range_list[i]}")
                sum = int(v) + int(range_list[i])
                sums.append(sum)
        #print(f"sums: {sums}")
        if int(numbers[stop]) not in sums:
            print(f"{int(numbers[stop])} is not a sum of the other numbers.")
            break
        stop = stop + 1
        start = start + 1
        
# part 1
number_not_a_sum(numbers, 0, 25)