import numpy as np
from itertools import groupby

def is_perfect_reflection(pattern):

    left_side_of_reflection  = []
    right_side_of_reflection = []

    for line_idx in range(len(pattern) - 1):
        if pattern[line_idx] == pattern[line_idx+1]:

            left_side_of_reflection  = pattern[:line_idx+1]
            right_side_of_reflection = pattern[line_idx+1:] 

    num_to_return = len(left_side_of_reflection)

    left_side_of_reflection = left_side_of_reflection[::-1]

    print("Left: ", left_side_of_reflection)
    print("Right: ", right_side_of_reflection)

    boundary = 0
    if len(left_side_of_reflection) < len(right_side_of_reflection):
        boundary = len(left_side_of_reflection)
        right_side_of_reflection = right_side_of_reflection[:boundary]
    else:
        boundary = len(right_side_of_reflection)
        left_side_of_reflection = left_side_of_reflection[:boundary]

    perfect_reflection_bool = False

    if left_side_of_reflection == right_side_of_reflection:
        perfect_reflection_bool = True

    if perfect_reflection_bool:
        return num_to_return
    else:
        return 0


file = open("input.txt", 'r')
input = file.read().splitlines()
patterns = [list(g) for k, g in groupby(map(str.strip, input), key=lambda line: line != '') if k]


sum = 0
for pattern in patterns:
    transposed_list = [''.join(s) for s in zip(*pattern)]
    num = 0
    if is_perfect_reflection(pattern) == 0:
        num = is_perfect_reflection(transposed_list)
    else:
        num = is_perfect_reflection(pattern) * 100
    sum += num

print(sum)








# Check if there is a relfection along y-axis or x-axis. One of them will create a perfect reflection (disocunting any extra rows)
# If vertical reflection, add up # of columns to the left
# If horizontal reflection, add up # of rows above
# total = # columns to left + (100 * rows above)