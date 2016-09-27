import math, sys

total_degrees, degrees_left, total_people, people_left = map(int, sys.argv[1:])

def get_equal_share(total_degrees, people):
  return int(math.ceil(total_degrees/float(people)))

def noms(total_degrees, degrees_left, people):
  bid = get_equal_share(total_degrees,people)-1
  return min(degrees_left, bid)

print noms(total_degrees, degrees_left, people_left)
