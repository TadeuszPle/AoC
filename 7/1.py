cards_names = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
card_vals = dict(zip(cards_names,range(14, 1, -1)))
# all of this can be simply done with binary search
# you just see if the longest count is different
# if it is you know which is better
# if it not then check for two paris and full houses
# if still the same go trough the actual strings and compare
# insert one by one with binary search
# sum all bids


class Hand:
    def __init__(self, value, bid):
        self.value: str = value
        self.bid: int = int(bid)
        self.type: int = self.get_type()
    
    def get_type(self) -> int:
        count = {}
        for c in self.value:
            if c in count:
                count[c] +=1
            else:
                count[c] = 1
        # one pair , two pairs
        if len(count.keys()) > 3:
            return 6 - len(count.keys())
        # two pairs, three of a kind
        elif len(count.keys()) == 3:
            if max(count.values()) == 2:
                return 3
            else:
                return 4
        # full house, four of a kind
        elif len(count.keys()) == 2:
            if max(count.values()) == 3:
                return 5
            else:
                return 6
        else:
            return 7
        

    def __eq__(self, other):
        return self.value == other.value
    
    def __gt__(self, other):
        if self.type == other.type:
            for c1, c2 in zip(self.value, other.value):
                if c1 == c2:
                    continue
                else:
                    return card_vals[c1] > card_vals[c2]  
            return False          
        else:
            return self.type > other.type
    def __lt__(self, other):
        if self.type == other.type:
            for c1, c2 in zip(self.value, other.value):
                if c1 == c2:
                    continue
                else:
                    return card_vals[c1] < card_vals[c2]
            return False           
        else:
            return self.type < other.type


with open('input.txt') as f:
    lines = f.readlines()
hands = []
for line in lines:
    new_hand = Hand(*line.split())
    hands.append(new_hand)

hands.sort()
print([( h.value, h.type) for h in hands])
cum_sum = sum([h.bid*(i+1) for i, h in enumerate(hands)])

print(cum_sum)
