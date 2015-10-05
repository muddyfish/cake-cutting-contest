import random, math

random_people = 2
perfect_people = 8
degrees = 360

def perfect_func(degrees_left, people):return int(math.ceil(degrees_left/(people+0.0)))
def random_func(degrees_left, people):return min(random.randrange(perfect_func(degrees_left,people)+1,perfect_func(degrees_left, people)*2), degrees_left)

def auction(random_people,perfect_people, degrees_left):
    people_funcs = [perfect_func]*perfect_people + [random_func]*random_people
    people = [func(degrees_left, perfect_people+random_people) for func in people_funcs]
    won = random.choice([(people_funcs[i],j) for i,j in enumerate(people) if people[i]==min(people)])
    if won[0] is perfect_func:
        perfect_people-=1
    else:
        random_people-=1
    print degrees_left, zip([f.__name__ for f in people_funcs], people)
    return won, perfect_people, random_people

true_won = [0,0]
i=0
while perfect_people!=0 or random_people!=0:
    won, perfect_people, random_people = auction(random_people,perfect_people,degrees)
    degrees -= won[1]
    print won[0].__name__, won[1]
    if won[1]> true_won[1]:
        true_won = won[0].__name__, won[1], i
    i+=1
print
print true_won
