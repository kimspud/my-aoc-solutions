# day 21 - in collaboration with SteveRu

full_ingredients = {}
somedict = {}

with open("day_21_input.txt", "r") as data:
    for line in data:
        ic = line.strip("\n").split("(contains")
        line_ingredients = ic[0].strip(" ").split(" ")
        line_contains = ic[1].replace(" ", "").replace(")", "").split(",")
        #print(f"li = {line_ingredients}, lc = {line_contains}")
        # convert line_ingredients to ingredient_set
        ingredient_set = set(line_ingredients)

        # build up full list with the number of times each ingredient appears
        for ingredient in line_ingredients:
            if ingredient in full_ingredients:
                full_ingredients[ingredient] = full_ingredients[ingredient] + 1
            else:
                full_ingredients[ingredient] = 1

        #print(f"ingredient_set {ingredient_set}")
        # build up set of possible ingredients per allergen,
        # using intersection over all ingredients where allergen is provided
        for allergen in line_contains:
            if allergen in somedict:
                somedict[allergen] = somedict[allergen].intersection(ingredient_set)
            else:
                somedict[allergen] = ingredient_set

         
    
    sorted_keys = sorted (somedict.keys())
    print (sorted_keys) 
    somelist = []
    for key in sorted_keys:
        somelist.append(list(somedict[key]))
    print(f"somelist = {somelist}")

    #print("--------------------------")
    #print(f"full_ingredients {full_ingredients}")

# remove ingredients that are possible allergens
remaining_ingredients = full_ingredients
for allergen_ingredient_set in somedict.values():
    for ingredient in allergen_ingredient_set:
        if ingredient in remaining_ingredients:
            del remaining_ingredients[ingredient]
        # ingredients.append(line.strip("\n").split("(contains")  

#print(f"remaining ingredients {remaining_ingredients}")

# add up the count of the remaining ingredients
count = 0
for val in remaining_ingredients.values():
    count += val
#print(f"ingredients: {ingredients}")

#print(f"final count {count}")









