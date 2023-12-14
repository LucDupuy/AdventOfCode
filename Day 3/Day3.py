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

    return (left in symbols_list or right in symbols_list or top in symbols_list or bottom in symbols_list or top_left in symbols_list or top_right in symbols_list or bottom_left in symbols_list or bottom_right in symbols_list)


file = open("input.txt", 'r')
list = file.read().splitlines()
symbols_list = '@#$%&*+=-_/'
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
    

sum = 0
for row_idx, row in enumerate(nums_in_row):
    if len(row) > 0:
        for num_idx, num in enumerate(row):
            adjaceny = False
            col_idx_of_first_digit = start_idx_of_nums_list[row_idx][num_idx]
            for col_idx in range(col_idx_of_first_digit, col_idx_of_first_digit+len(num)):
                if check_surrounding(row_idx=row_idx, col_idx=col_idx, num=num) == True:
                    adjaceny = True
                    break
            if adjaceny == True:
                sum += int(num)
print(sum)