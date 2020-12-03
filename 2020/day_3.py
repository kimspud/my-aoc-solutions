# Day 3
# Starting at the top-left corner of your map and following a slope of right 3 and down 1, 
# how many trees would you encounter?  Trees are represented as # in dataset.
terrain_map = []
product = 1

# read input file and make list from input
with open("day3_input.txt", "r") as input:
    for line in input:
        terrain_map.append(line.replace("\n", ""))

#find out where bottom of map is
length = len(terrain_map)

def tree_count(move_down, move_right):
    column_index = 0
    row_index = 0
    tree_count = 0
    while row_index < length:
        row = terrain_map[row_index]
        coordinate_value = row[column_index % len(row)]
        if coordinate_value == "#":
            tree_count = tree_count + 1
        row_index = row_index + move_down
        column_index = column_index + move_right
    return(tree_count)

product = tree_count(1,1)
product = product * tree_count(1,3)
product = product * tree_count(1,5)
product = product * tree_count(1,7)
product = product * tree_count(2,1)
print(product)