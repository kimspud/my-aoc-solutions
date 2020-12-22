# day 22

deck_player_1 = [38, 1, 28, 32, 43, 21, 42, 29, 18, 13, 39, 41, 49, 31, 19, 26, 27, 40, 35, 14, 3, 36, 12, 16, 45]
deck_player_2 = [34, 15, 47, 20, 23, 2, 11, 9, 8, 7, 25, 50, 48, 24, 46, 44, 10, 6, 22, 5, 33, 30, 4, 17, 37,]
length_1 = len(deck_player_1)
length_2 = len(deck_player_2)
result = 0
turn_count = 0
i = 0

while len(deck_player_1) >= 1 and len(deck_player_2) >= 1:
    length_1 = len(deck_player_1)
    length_2 = len(deck_player_2)
    print(f"turn count {turn_count}")
    if deck_player_1[0] > deck_player_2[0]:
        print("player 1 wins this round")
        deck_player_1.insert(length_1, deck_player_1.pop(0))
        deck_player_1.insert(length_1, deck_player_2.pop(0))
    elif deck_player_1[0] < deck_player_2[0]:
        print("player 2 wins this round")
        deck_player_2.insert(length_2, deck_player_2.pop(0))
        deck_player_2.insert(length_2, deck_player_1.pop(0))
    else:
        print("there is a tie")
    print(f"deck_player_1 {deck_player_1}")
    print(f"deck_player_2 {deck_player_2}")
    print("-------------------")
    turn_count += 1

if len(deck_player_1) is not 0:
    winning_deck = deck_player_1
else:
    winning_deck = deck_player_2
print(f"winning deck is: {winning_deck}")

reversed_deck = [ele for ele in reversed(winning_deck)]

for i in range(0, len(winning_deck)):
    result = result + ((i + 1) * reversed_deck[i])

print(f"result: {result}")