""" Find LCM of multiple numbers """


def find_lcm(x, y) :
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

""" list = [4, 8, 5, 10] """
list = []

num = int(input("Enter the number items per array:"))
print("Enter numbers")
for i in range(0, num) :
    num = int(input())
    list.append(num)

x = list[0]
y = list[1]

lcm = find_lcm(x, y)

for i in range(2, len(list)) :
    lcm = find_lcm(lcm, list[i])

print("L.C.M is ", lcm)
