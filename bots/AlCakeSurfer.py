import sys, math

total_degrees, degrees_left, total_people, people_left = map(int, sys.argv[1:])

fraction_left = (degrees_left + 0.0)/ total_degrees
fraction_gone = 1.0 - fraction_left
fair_share = fraction_left/people_left
modified_fair_share = fair_share + 0.05

weighting = 0.5 * fraction_gone + 0.5 - modified_fair_share
surfing = (math.cos(fraction_gone * math.pi))**2

print(int(math.floor((weighting * surfing + modified_fair_share)* total_degrees)))
