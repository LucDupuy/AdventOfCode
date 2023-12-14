from collections import Counter

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
    "T": 0,
    "9": 0,
    "8": 0,
    "7": 0,
    "6": 0,
    "5": 0,
    "4": 0,
    "3": 0,
    "2": 0,
    "J": 0,
}
    for card in hand:
        cards_map[card] +=1

    for card, count in cards_map.items():
        if hand.count("J") == 5 or hand.count("J") == 4 or (hand.count("J") == 3 and len(set(hand)) == 2) or (hand.count("J") == 2 and len(set(hand))) == 2 or (hand.count("J") == 1 and len(set(hand)) == 2):
           hand_type_map[hand] = "7_5 of a kind"
        elif hand.count("J") == 3 or (hand.count("J") == 2 and len(set(hand)) == 3):
            hand_type_map[hand] = "6_4 of a kind"

        elif (hand.count("J") == 1 and len(set(hand)) == 3):
            frequency_dict = Counter(hand)
            x = max(frequency_dict, key= lambda x: frequency_dict[x])
            if frequency_dict[x] == 3:
                hand_type_map[hand] = "6_4 of a kind"
            else:
                hand_type_map[hand] = "5_full house"
        elif (hand.count("J") == 2 and len(set(hand)) == 4) or (hand.count("J") == 1 and len(set(hand)) == 4):
            hand_type_map[hand] = "4_3 of a kind"
        elif hand.count("J") == 1 and len(set(hand)) == 5:
            hand_type_map[hand] = "2_pair"
        elif len(set(hand)) == len(hand):
            hand_type_map[hand] = "1_high card"
        elif count == 5:
            hand_type_map[hand] = "7_5 of a kind"
        elif count == 4:
            hand_type_map[hand] = "6_4 of a kind"
        elif count == 3:
            if sum(x == 0 for x in cards_map.values()) == 10:
                hand_type_map[hand] = "4_3 of a kind"
            else:
                hand_type_map[hand] = "5_full house"
        elif count == 2: 
            if sum(x == 0 for x in cards_map.values()) == 9:
                hand_type_map[hand] = "2_pair"
            else:
                if hand not in hand_type_map:
                    hand_type_map[hand] = "3_2 pair"

buckets = [[] for i in range(7)]


for hand, type in hand_type_map.items():
    if type == "1_high card":
        buckets[0].append(hand)
    elif type == "2_pair":
        buckets[1].append(hand)
    elif type == "3_2 pair":
        buckets[2].append(hand)
    elif type == "4_3 of a kind":
        buckets[3].append(hand)
    elif type == "5_full house":
        buckets[4].append(hand)
    elif type == "6_4 of a kind":
        buckets[5].append(hand)
    elif type == "7_5 of a kind":
        buckets[6].append(hand)

sorted_buckets = [[] for i in range(7)]
custom_alphabet = "J23456789TQKA"


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