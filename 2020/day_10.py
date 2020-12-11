# day 10
from itertools import combinations

my_adapters = []
current_jolt_rating = 0


with open("day_10_input.txt", "r") as data:
    for line in data:
        my_adapters.append(line.strip("\n"))

def part_1(my_adapters, current_jolt_rating):
    # make the list a list of int's
    for i in range(0, len(my_adapters)): 
        my_adapters[i] = int(my_adapters[i]) 
    my_adapters = sorted(my_adapters)
    #print(f"my adapters: {my_adapters}")
    current_jolt_ratings = [(current_jolt_rating + 1), (current_jolt_rating + 2), (current_jolt_rating + 3)]
    differences = []
    # find joltage of built-in-adapter
    built_in_adapter = max(my_adapters) + 3
    #print(f"built_in_adapter: {built_in_adapter}")

    if built_in_adapter != current_jolt_ratings[2]:
        for adapter in my_adapters:
            #print(f"current_jolt_rating: {current_jolt_rating}")
            #print(f"current_jolt_ratings: {current_jolt_ratings}")
            #print(f"adapter: {adapter}")
            if adapter in current_jolt_ratings:
                matches = []
                matches.append(adapter)
                #print(f"match: {matches}")
                for match in matches:
                    if match - current_jolt_rating == 1:
                        differences.append(match - current_jolt_rating)
                        current_jolt_rating = match
                    elif match - current_jolt_rating == 2:
                        differences.append(match - current_jolt_rating)
                        current_jolt_rating = match
                    elif match - current_jolt_rating == 3:
                        differences.append(match - current_jolt_rating)
                        current_jolt_rating = match
                    #print(f"differences: {differences}")
                current_jolt_ratings = [(current_jolt_rating + 1), (current_jolt_rating + 2), (current_jolt_rating + 3)]
            #print("-----------------------")
    # count the jolt differences of 1
    count_of_1 = differences.count(1)
    print(f"count of differences of 1: {count_of_1}")
    # count the jolt differences of 3. Add one for the built_in_adapter.
    count_of_3 = differences.count(3) + 1
    print(f"count of differences of three: {count_of_3}")
        
    result = count_of_1 * count_of_3
    print(f"result: {result}")

def find_combo(my_adapters, current_jolt_rating, built_in_device):
    print(f"current_jolt_rating: {current_jolt_rating}")
    print(f"built_in_device: {built_in_device}")
    if current_jolt_rating + 3 == int(built_in_device):
        return 1

    next_max = current_jolt_rating + 3
    print(f"next_max: {next_max}")
    match_count = 0
    comb = []
    for n in range(0,len(my_adapters)+1):
        comb.append([i for i in combinations(my_adapters,n)])
    print(f"combinations: {comb}")
    print(f"combinations_length: {len(comb)}")
    
    for list in comb:
        new_adapters = list
        print(f"new_adapters: {new_adapters}")
        #for new_adapter in new_adapters:
            
            #print(f"adapter: {new_adapter}")
            #while adapter != next_max:
                    
def part_2(my_adapters):
    for i in range(0, len(my_adapters)): 
        my_adapters[i] = int(my_adapters[i]) 
    my_adapters = sorted(my_adapters)
    built_in_adapter = max(my_adapters) + 3
    current_jolt_rating = 0
    
    find_combo(my_adapters, current_jolt_rating, built_in_adapter)

#part_1(my_adapters, current_jolt_rating)
part_2(my_adapters)
