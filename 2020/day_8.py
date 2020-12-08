# day 8

instruction_map = []
instruction_run_once = []
index = 0
accumulator = 0

with open("day_8_input.txt", "r") as data:
    for line in data:
        instruction_map.append(line.strip("\n").replace("+", "").split(" "))

while index < len(instruction_map):
    instruction = instruction_map[index]
    # print(f"instruction: {instruction}")
    # print(f"instruction_run_once_list {instruction_run_once}")

    if index in instruction_run_once:
        print("this is the end")
        print(f"accumulator: {accumulator}")
        break

    instruction_run_once.append(index)
    if instruction[0] == "acc":
        accumulator = accumulator + int(instruction[1])
        index = index + 1
    elif instruction[0] == "jmp":
        index = index + int(instruction[1])
    elif instruction[0] == "nop":
        index = index + 1



