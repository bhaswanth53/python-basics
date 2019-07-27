""" LCM of two numbers """

"""
    1. greater number = greater(x, y)
    2. If (greater % x == 0) and (greater % y == 0) then lcm is greater
    3. Else increase the number until divisible by both
"""

def lcm(x, y) :
    if(x > y) :
        greater = x
    else :
        greater = y
    
    while(True) :
        if((greater % x == 0) and (greater % y == 0)) :
            lcm = greater
            break
        greater += 1

    return lcm

x = int(raw_input("Enter the value of x\n"))
y = int(raw_input("\nEnter the value of y\n"))

lcm = lcm(x, y)
print "L.C.M of ", x, " and ", y, " is ", lcm