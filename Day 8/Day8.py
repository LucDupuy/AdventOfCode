file = open("input.txt", 'r')
list = file.read().splitlines()
list = [i for i in list if i]

steps = list[0]
list.pop(0)

rule_map = {}

for rule in list:
    rule = rule.split("=")
    tmp = rule[1].strip(" (")
    tmp = tmp.strip(")")
    tmp = tmp.split(",")
    rule_map[rule[0].strip(' ')] = (tmp[0], tmp[1].strip(' '))

count = 0
current_location = "AAA"

while current_location != "ZZZ":
    for step in steps:
        if step == "L":
            next_location = rule_map[current_location][0]
            current_location = next_location
            count +=1
        else:
            next_location = rule_map[current_location][1]
            current_location = next_location
            count +=1
print(count)