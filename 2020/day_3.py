# Day 3
# Starting at the top-left corner of your map and following a slope of right 3 and down 1, 
# how many trees would you encounter?  Trees are represented as # in dataset.

terrain_map = []
column = 0
row = 0

# read input file and make list from input
with open("day3_input.txt", "r") as input:
    for line in input:
        terrain_map.append(line)
        
terrain_map.remove('\n')       
print(str(terrain_map[1]))

#find out where bottom of map is
destination = len(terrain_map) + 1
print("destination is: " + str(destination))



