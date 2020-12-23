# day 23
# This solution is super ugly

cup_labels = [3, 6, 4, 2, 9, 7, 5, 8, 1]
print(f"original cup labels {cup_labels}")
current_cup = cup_labels[0]
picked_up_cup_indices = []
picked_up_cups = []
destination_cup = ""
move = 0

while move < 101:
    #designate current cup
    print(f"cup labels {cup_labels}")
    print(f"current cup value {current_cup}") #debug
    print(f"current cup index {cup_labels.index(current_cup)}") #debug
    current_cup_index = cup_labels.index(current_cup)
    print(f"min label {min(cup_labels)}")
    print(f"max label {max(cup_labels)}")

    #remove three numbers to the right of current cup and store
    picked_up_cups_indices = [(current_cup_index + 1) % len(cup_labels), (current_cup_index + 2) % len(cup_labels), 
                                (current_cup_index + 3) % len(cup_labels)] #debug
    print(f"picked up cups indices {picked_up_cups_indices}") #debug
    picked_up_cups = [cup_labels[(current_cup_index + 1) % len(cup_labels)], 
                        cup_labels[(current_cup_index + 2) % len(cup_labels)], cup_labels[(current_cup_index + 3) % len(cup_labels)]]
    
    for i in picked_up_cups:
        cup_labels.remove(i)
    print(f"picked up cups {picked_up_cups}")
    print(f"cup labels {cup_labels}")

    #find destination cup
    destination_cup = current_cup - 1

    if destination_cup < min(cup_labels):
        destination_cup = max(cup_labels)

    while destination_cup in picked_up_cups:
        if destination_cup >= min(cup_labels):
            destination_cup = destination_cup - 1
            #print(f"destination cup {destination_cup}")
        else:
            destination_cup = max(cup_labels)
    print(f"destination cup {destination_cup}")

    #insert picked up cups
    for label in cup_labels:
        if label == destination_cup:
            index = cup_labels.index(label)
            cup_labels.insert(index + 1, picked_up_cups[0])
            cup_labels.insert(index + 2, picked_up_cups[1])
            cup_labels.insert(index + 3, picked_up_cups[2])

    #set new current cup value
    current_cup = cup_labels[((cup_labels.index(current_cup)) + 1) % len(cup_labels)]
    print(f"new current cup index {cup_labels.index(current_cup) + 1}")
    print(f" new current_cup {current_cup}")

    move += 1
    print(f"move {move}")
    print("-----------------")

