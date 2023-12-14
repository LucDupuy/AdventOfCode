import time

def updateWinningNums(list):
    total_winning_nums = []
    for _, card in enumerate(list):

        card = card.split(':', 1)[-1]
        
        winning_nums = card.split('|')[0]
        my_nums = card.split('|')[1]
        
        winning_nums = winning_nums.split(' ')
        winning_nums = [x for x in winning_nums if x != ""]

        my_nums = my_nums.split(' ')
        my_nums = [x for x in my_nums if x != ""]

        total_winning_nums.append(len(set(my_nums).intersection(winning_nums))) 

    return total_winning_nums






def makeDuplicates(number_of_cards_to_add, current_card_number, base_list):


    current_card_number = int(current_card_number.split(':', 1)[0][5:])
    return(base_list[current_card_number:current_card_number+number_of_cards_to_add])    




    # print(number_of_cards_to_add)
    # penis = current_card_number.split(':', 1)[0][5:]
    # penis = int(penis)

    # return base_list[penis:penis+number_of_cards_to_add]
 





start = time.time()
print("Start Time: ", start)

file = open("input.txt", 'r')
list = file.read().splitlines()
base_list = list.copy()
list_of_winning_nums = updateWinningNums(list)
total = 0





dups = []
for num in list_of_winning_nums:

    tmp = makeDuplicates(num, list[0], base_list=base_list)
    for dup_card in tmp:
        dups.append(dup_card)
    list.pop(0)

total += len(dups)


def doesthings(list, dups, list_of_winning_nums):
    for num in list_of_winning_nums:
        tmp = makeDuplicates(num, list[0], base_list=base_list)
        for dup_card in tmp:
            dups.append(dup_card)
        list.pop(0)

    return dups



while len(list_of_winning_nums) > 0:
    list = dups
    dups = []
    list_of_winning_nums = updateWinningNums(list)
    dups = doesthings(list=list, dups=[], list_of_winning_nums=list_of_winning_nums)
    total += len(dups)
    print(total)



print(total + len(base_list))



end = time.time()
print("End Time: ", end)

print("Execution Time: ", end - start)
