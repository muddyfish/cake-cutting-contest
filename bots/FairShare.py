import sys

def FairShare(TotalDegrees, DegreesLeft, TotalPeople, PeopleLeft):

    FairShare = TotalDegrees / TotalPeople
    FairShareNow = DegreesLeft / PeopleLeft

    if PeopleLeft == 1:
        return DegreesLeft

    elif FairShare > FairShareNow:
        return FairShare

    elif FairShare == FairShareNow:
        return FairShare

    elif FairShare < FairShareNow:
        return FairShareNow

print FairShare(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
