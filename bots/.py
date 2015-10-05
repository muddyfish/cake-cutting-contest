import random, math, sys

total_degrees, degrees_left, total_people, people_left = map(int, sys.argv[1:])

def get_equal_share(degrees_left, people):
    return int(math.ceil(degrees_left/float(people)))

def get_greedy(degrees_left, people):
    min_bid = get_equal_share(degrees_left,people)+1
    max_bid = min_bid*2
    bid = random.randrange(min_bid, max_bid)
    return min(bid, degrees_left)

print get_greedy(degrees_left, people_left)
