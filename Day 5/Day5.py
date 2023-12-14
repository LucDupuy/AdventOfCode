def dostuff(current_map, src_list):
    #src_list is the initial seeds list and then subsequent destinations that become srcs
    dst =  []
    dst_ranges = []
    src_ranges = []
    for rule in current_map:
        split_rule = rule.split(" ")
        dst_start = int(split_rule[0])
        dst_end   = int(split_rule[0]) + int(split_rule[2])
        src_start = int(split_rule[1])
        src_end   = int(split_rule[1]) + int(split_rule[2])

        dst_ranges.append((dst_start, dst_end))
        src_ranges.append((src_start, src_end))

    for src in src_list:
        in_rules = False
        for idx, src_range in enumerate(src_ranges):
            if src in range(src_range[0], src_range[1]):
                #Adding dst_idx to the start of the dst range gets us the matching dst for the given src
                offset = src-src_range[0]
                dst.append(dst_ranges[idx][0] + offset)
                in_rules = True
                break
        if not in_rules:
            dst.append(src)
                
    return dst

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



for idx, map in enumerate(master_maps_list):
    dst = dostuff(map, src_list=src_list)
    src_list = dst
print(min(dst))