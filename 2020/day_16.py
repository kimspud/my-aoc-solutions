# day 16

rules = list(range(25, 975))
nearby_tickets = []
error_rate = 0

with open("day_16_input.txt", "r") as data:
    temp = data.read().replace("\n", ",")
    nearby_tickets = list(temp.split(','))
print(nearby_tickets)

nearby_tickets = list(map(int, nearby_tickets)) 

for number in nearby_tickets:
    if number not in rules:
        invalid = number
        print(f"invalid: {invalid}")
        error_rate = error_rate + int(invalid)
print(f"error_rate {error_rate}")