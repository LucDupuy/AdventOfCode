def get_val(passed_line):
    current_line = passed_line
    new_list = [current_line]

    while (all(ele == current_line[0] for ele in current_line) and current_line[0] == 0) == False:
        tmp = []
        for i in range(len(current_line) - 1):
            tmp.append(current_line[i+1] - current_line[i])
        new_list.append(tmp)
        current_line = tmp
        

    for line in new_list:
        line.append(0)


    new_list = new_list[::-1]

    for idx, line in enumerate(new_list):
        if all(v == 0 for v in line):
            continue
        left = line[-2]
        bottom = new_list[idx-1][-1]
        line[-1] = left + bottom
      
    new_list = new_list[::-1]    

    return new_list[0][-1]




file = open("input.txt", 'r')
list = file.read().splitlines()
list_of_ints = []
for line in list:
    list_of_ints.append([int(element) for element in line.split()])

total = 0
for line in list_of_ints:
    x = get_val(line[::-1])
    total +=x
print(total)
