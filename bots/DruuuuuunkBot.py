import sys,random
tD,dL,pN,pL=map(int,sys.argv[1:])
a=dL/(pL+1)
if a < 0:
 a = dL
print(a)
