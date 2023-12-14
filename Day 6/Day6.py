file = open("input.txt", 'r')
list = file.read().splitlines()

times_list = list[0].split(':', 1)[-1]
times_list = times_list[1:]
times_list = times_list.split(" ")

distance_list = list[1].split(':', 1)[-1]
distance_list = distance_list[1:]
distance_list = distance_list.split(" ")

tmp = []
for x in times_list:
    if x.isdigit():
        tmp.append(int(x))
times_list = tmp

tmp = []
for x in distance_list:
    if x.isdigit():
        tmp.append(int(x))
distance_list = tmp





time_1 = times_list[0]
time_2 = times_list[1]
time_3 = times_list[2]
time_4 = times_list[3]

distance_1 = distance_list[0]
distance_2 = distance_list[1]
distance_3 = distance_list[2]
distance_4 = distance_list[3]

race_1_winning_nums = []
for x in range(1, time_1):
    if (x * (time_1-x)) > distance_1:
        race_1_winning_nums.append(x)

race_2_winning_nums = []
for x in range(1, time_2):
    if (x * (time_2-x)) > distance_2:
        race_2_winning_nums.append(x)

race_3_winning_nums = []
for x in range(1, time_3):
    if (x * (time_3-x)) > distance_3:
        race_3_winning_nums.append(x)

race_4_winning_nums = []
for x in range(1, time_4):
    if (x * (time_4-x)) > distance_4:
        race_4_winning_nums.append(x)

print (len(race_1_winning_nums) * len(race_2_winning_nums) * len(race_3_winning_nums) * len(race_4_winning_nums))
