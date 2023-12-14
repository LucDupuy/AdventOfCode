file = open("input.txt", 'r')
list = file.read().splitlines()

hands_list = []
bids_list = []

hand_type_map = dict()

for line in list:
    line = line.split(" ")
    hands_list.append(line[0])
    bids_list.append(line[1])


hand_bid_map  = {hands_list[i]: bids_list[i] for i in range(len(hands_list))}

for hand in hands_list:
    cards_map = {
    "A": 0,
    "K": 0,
    "Q": 0,
    "J": 0,
    "T": 0,
    "9": 0,
    "8": 0,
    "7": 0,
    "6": 0,
    "5": 0,
    "4": 0,
    "3": 0,
    "2": 0,
}
    for card in hand:
        cards_map[card] +=1

    for card, count in cards_map.items():

        if len(set(hand)) == len(hand):
            hand_type_map[hand] = "1_High Card"
        elif count == 5:
            hand_type_map[hand] = "7_5 of a kind"
        elif count == 4:
            hand_type_map[hand] = "6_4 of a kind"
        elif count == 3:
            if sum(x == 0 for x in cards_map.values()) == 10:
                hand_type_map[hand] = "4_3 of a Kind"
            else:
                hand_type_map[hand] = "5_Full House"
        elif count == 2: 
            if sum(x == 0 for x in cards_map.values()) == 9:
                hand_type_map[hand] = "2_Pair"
            else:
                if hand not in hand_type_map:
                    hand_type_map[hand] = "3_2 Pair"


print(hand_type_map)
#buckets = high card, pair, two pair, three of a kind, full house, four of a kind, five of a kind
buckets = [[] for i in range(7)]

for hand, type in hand_type_map.items():
    if type == "1_High Card":
        buckets[0].append(hand)
    elif type == "2_Pair":
        buckets[1].append(hand)
    elif type == "3_2 Pair":
        buckets[2].append(hand)
    elif type == "4_3 of a Kind":
        buckets[3].append(hand)
    elif type == "5_Full House":
        buckets[4].append(hand)
    elif type == "6_4 of a kind":
        buckets[5].append(hand)
    elif type == "7_5 of a kind":
        buckets[6].append(hand)

sorted_buckets = [[] for i in range(7)]
custom_alphabet = "23456789TJQKA"


for idx, bucket in enumerate(buckets):
    sorted_buckets[idx] = sorted(bucket, key=lambda hand: [custom_alphabet.index(card) for card in hand])

final_list = []

for bucket in sorted_buckets:
    for hand in bucket:
        final_list.append(hand)

total = 0

for idx, hand in enumerate(final_list):
    
    rank = idx+1
    bid  = int(hand_bid_map[hand])

    total += rank*bid
print(total)