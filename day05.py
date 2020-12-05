input_data = """FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""

with open('adventofcode20/day05_input.txt', 'r') as f:    
    input_data = f.read()

passes = input_data.split()

max_id = 0

def get_seat_id(boarding_pass):
    row = boarding_pass[:7].replace('F', '0').replace('B','1')
    row = int(row,2)

    column = boarding_pass[7:].replace('R', '1').replace('L','0')
    column = int(column,2)

    seat = row * 8 + column

    return seat

max_seat = max(passes, key = get_seat_id)

print(get_seat_id(max_seat))


