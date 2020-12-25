value = 1
subject_number = 7
door_loop_size = None
card_loop_size = None
card_public_key = 19774466
door_public_key = 7290641

value = 1
for j in range(100000000):
    value *= subject_number
    value = value % 20201227
    if value == card_public_key:
        card_loop_size = j + 1
    if value == door_public_key:
        door_loop_size = j + 1
    if card_loop_size and door_loop_size:
        break

print(subject_number, card_loop_size, door_loop_size, card_public_key, door_public_key)
# Get encription key #1
subject_number = door_public_key
value = 1
for j in range(card_loop_size):
    value *= subject_number
    value = value % 20201227
print(value)

# Get encription key #2
value = 1
subject_number = card_public_key
for j in range(door_loop_size):
    value *= subject_number
    value = value % 20201227
print(value)