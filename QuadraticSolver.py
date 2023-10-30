# Spencer Gaffin
# QuadraticSolver

import math

a = int(input("Input A value "))
b = int(input("Input B value "))
c = int(input("Input C value "))

if a == type(str):
    print ("Please enter a number")

d = b**2-4*a*c

if d < 0:
    print ("This equation has no solution")
elif d == 0:
    ans0 = (-b + math.sqrt(d))/(2*a)
    print ("There is one soulution: ", ans0)
else:
    ans1 = (-b + math.sqrt(d))/(2*a)
    ans2 = (-b - math.sqrt(d))/(2*a)
    print ("There are two solutions:", ans1, "and", ans2) 

