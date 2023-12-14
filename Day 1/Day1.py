file = open("input.txt", 'r')
list = file.read().splitlines()

sum = 0

for word in list:
    tmp_list = []
    for char in word:
        if char.isdigit():
            tmp_list.append(char)
    if len(tmp_list) > 1:
        tmp_val = tmp_list[0] + tmp_list[-1]
        sum += int(tmp_val)

    if len(tmp_list) == 1:
        tmp_val = tmp_list[0] + tmp_list[0]
        sum += int(tmp_val)

print(sum)

file.close()