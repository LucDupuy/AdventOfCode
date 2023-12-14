def get_maps():
    file = open("input.txt", 'r')
    list = file.read().splitlines()
    seeds_list = list[0].split(':', 1)[-1]
    seeds_list = seeds_list[1:]
    seeds_list = seeds_list.split(" ")
    seeds_list = [eval(i) for i in seeds_list]
    list = list[2:]

    for item in list:
        if len(item) > 0 and item[0].isalpha():
            list.remove(item)
    list.append("")
    tmp = []
    master_maps_list = []
    for item in list:
        if len(item) > 0:
            tmp.append(item)
        if len(item) == 0:
            master_maps_list.append(tmp)
            tmp = []


    return seeds_list, master_maps_list


dst = []
src_list, master_maps_list = get_maps()



