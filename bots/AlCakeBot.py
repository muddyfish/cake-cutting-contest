import sys, math

total_degrees, degrees_left, total_people, people_left = map(int, sys.argv[1:])

fraction_left = (degrees_left + 0.0)/ total_degrees
fraction_gone = 1.0 - fraction_left

factor = (math.sin(fraction_gone * math.pi / 2.0))**2
fraction = (factor/2.0) + 0.5

if total_degrees == degrees_left:
   print(int(math.floor(total_degrees/2.0) - 1))
else:
   print(int(math.floor(degrees_left * fraction)))
