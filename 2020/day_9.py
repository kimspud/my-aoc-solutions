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
        #print(f"range_list: {range_list}")
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
            return int(numbers[stop])
        stop = stop + 1
        start = start + 1


def part_2(numbers, invalid_number):
    #print(f"numbers + {numbers}")
    
    temp = []   # just gets rid of a warning

    for i in range(0, len(numbers)):
        temp = []
        j = i
        sum = 0
        while sum < invalid_number:
            value = int(numbers[j])
            sum = sum + value
            # print("value: " + str(value) + " sum: " + str(sum))
            temp.append(value)
            j = j + 1
        
        # print(f"sum is {sum}")
        if (sum == invalid_number):
            break

    result = max(temp) + min(temp)
    print("result: " + str(result))

        
# part 1
number_not_a_sum(numbers, 0, 25)

# part 2
part_2(numbers, 756008079)
