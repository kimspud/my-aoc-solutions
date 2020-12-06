#day_5
row_code = []
column_code = []
seat_codes = []
max_row = 127
min_row = 0
max_column = 7
min_column = 0
seat_ids = []

def find_row(row_code, max_row, min_row):
    for r in row_code:
        mid = (min_row + max_row) // 2
        if r == "F": 
            max_row = mid   
        elif r == "B":
            min_row = mid  + 1
        else:
            print("else")
    if max_row != min_row:
        print("something is wrong")
    return(max_row)
    
def find_column(column_code, max_column, min_column):
    for c in column_code:
        mid = (min_column + max_column) // 2
        if c == "L": 
            max_column = mid    
        elif c == "R":
            min_column = mid + 1
        else:
            print("else")
    if max_column != min_column:
        print("something is wrong")
    return(max_column)


with open("day_5_input.txt", "r") as data:
    for line in data:
        seat_codes.append(line.strip())
    #passports = input.replace('\n', ' ')

for code in seat_codes:
    seat_code = code
    row_code = []
    column_code = []
    for char in seat_code:
        if char == "B" or char == "F":
            row_code.append(char)
        else:
            column_code.append(char)
    row = find_row(row_code, max_row, min_row)
    column = find_column(column_code, max_column, min_column)
    seat_id =  row * 8 + column
    seat_ids.append(seat_id)
print("part_1 " + (str(max(seat_ids))))
seat_ids = sorted(seat_ids)
print("part_2 " + str(sorted(set(range(seat_ids[0], seat_ids[-1])) - set(seat_ids))))
    