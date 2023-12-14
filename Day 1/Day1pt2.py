nums_list = {
    "one": "one1one",
    "two": "two2two", 
    "three": "three3three", 
    "four": "four4four", 
    "five": "five5five",
    "six": "six6six", 
    "seven": "seven7seven", 
    "eight": "eight8eight",
     "nine": "nine9nine"
}



file = open("input.txt", 'r')
list = file.read().splitlines()

sum = 0

for word in list:
    for key, value in nums_list.items():
        word = word.replace(key, value)


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