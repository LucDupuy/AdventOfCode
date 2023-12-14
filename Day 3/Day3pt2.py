import re

def check_surrounding(col_idx, row_idx, num):
    left         = buffered_list[row_idx][col_idx-1]
    right        = buffered_list[row_idx][col_idx+1]
    top          = buffered_list[row_idx-1][col_idx]
    bottom       = buffered_list[row_idx+1][col_idx]
    top_left     = buffered_list[row_idx-1][col_idx-1]
    top_right    = buffered_list[row_idx-1][col_idx+1]
    bottom_left  = buffered_list[row_idx+1][col_idx-1]
    bottom_right = buffered_list[row_idx+1][col_idx+1]

    gear_location = ()

    if left is gear:  gear_location = (row_idx, col_idx-1)
    elif right is gear:  gear_location = (row_idx, col_idx+1)
    elif top is gear:  gear_location = (row_idx-1, col_idx)
    elif bottom is gear:  gear_location = (row_idx+1, col_idx)
    elif top_left is gear:  gear_location = (row_idx-1, col_idx-1)
    elif top_right is gear:  gear_location = (row_idx-1, col_idx+1)
    elif bottom_left is gear:  gear_location = (row_idx+1, col_idx-1)
    elif bottom_right is gear: gear_location = (row_idx+1, col_idx+1)

    if len(gear_location) != 0:
        if gear_location not in adjacency_map:
            adjacency_map[gear_location] = [num]
        else:
            if (num not in adjacency_map[gear_location]):
                adjacency_map[gear_location].append(num)

file = open("input.txt", 'r')
list = file.read().splitlines()
gear = '*'
length = len(list) + 2
buffer_str = "." * length
buffered_list = []

for line in list:
    new_line = "." + line + "."
    buffered_list.append(new_line)

buffered_list.append(buffer_str)
buffered_list.insert(0, buffer_str)

nums_in_row = []
start_idx_of_nums_list = []

for row_idx, line in enumerate(buffered_list):
    nums_in_row.append(re.findall(r'[0-9]+', line))

for row_idx, line in enumerate(buffered_list):
    start_idx_of_nums_list.append([num.start() for num in re.finditer(r'[0-9]+', line)])
    
adjacency_map = {}

for row_idx, row in enumerate(nums_in_row):
    if len(row) > 0:
        for num_idx, num in enumerate(row):
            adjacency = False
            col_idx_of_first_digit = start_idx_of_nums_list[row_idx][num_idx]
            for col_idx in range(col_idx_of_first_digit, col_idx_of_first_digit+len(num)):
                check_surrounding(row_idx=row_idx, col_idx=col_idx ,num=num)
total = 0
for key, value in adjacency_map.items():
    if len(value) > 1:
        product = 1
        for num in value:
             product *= int(num)
        total += product
print(total)