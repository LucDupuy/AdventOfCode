import numpy as np

file = open("input.txt", 'r')
list = file.read().splitlines()

galaxy_locations = []
num_galaxies = 0
distances = []
empty_rows_list = []
empty_columns_list = []

for row_idx, row in enumerate(list):
    for col_idx, col in enumerate(list):
        if list[row_idx][col_idx] == "#":
            num_galaxies += 1
            galaxy_locations.append((row_idx, col_idx))

for i in range(0, num_galaxies):
    for j in range(i+1, num_galaxies):
        start_row, start_col, end_row, end_col = galaxy_locations[i][0], galaxy_locations[i][1], galaxy_locations[j][0], galaxy_locations[j][1]
        distances.append(abs((start_row - end_row)) + abs((start_col-end_col)))



for row_idx, row in enumerate(list):
   if all(ele == "." for ele in row):
       empty_rows_list.append(row_idx)