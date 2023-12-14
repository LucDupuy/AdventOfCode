file = open("input.txt", 'r')
list = file.read().splitlines()

times_list = list[0].split(':', 1)[-1]
times_list = times_list[1:]
times_list = times_list.split(" ")

distance_list = list[1].split(':', 1)[-1]
distance_list = distance_list[1:]
distance_list = distance_list.split(" ")

times_str = ""
for x in times_list:
    if x.isdigit():
        times_str += x

distance_str = ""
for x in distance_list:
    if x.isdigit():
        distance_str += x
    

time = int(times_str)
distance = int(distance_str)



race_1_winning_nums = []
for x in range(1, time):
    if (x * (time-x)) > distance:
        race_1_winning_nums.append(x)



print (len(race_1_winning_nums))
