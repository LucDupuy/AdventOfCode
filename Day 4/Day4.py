file = open("input.txt", 'r')
list = file.read().splitlines()


sum = 0
for card_idx, card in enumerate(list):

    card = card.split(':', 1)[-1]
    
    winning_nums = card.split('|')[0]
    my_nums = card.split('|')[1]
    
    winning_nums = winning_nums.split(' ')
    winning_nums = [x for x in winning_nums if x != ""]

    my_nums = my_nums.split(' ')
    my_nums = [x for x in my_nums if x != ""]

    set_of_winning_nums_I_have = set(my_nums).intersection(winning_nums)
    
    if len(set_of_winning_nums_I_have) == 0:
        continue
    if len(set_of_winning_nums_I_have) == 1:
        sum +=1
    elif len(set_of_winning_nums_I_have) == 2:
        sum+=2
    else:
        sum += 2**(len(set_of_winning_nums_I_have) - 1)    

print(sum)