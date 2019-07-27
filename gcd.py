""" Find GCD(Greatest Common Divisor) of multiple numbets """

def gcd(x, y) :
    while(y) : 
        x, y = y, x % y

    return x

list = []

num = int(input("Enter the number items per array:"))
print("Enter numbers")
for i in range(0, num) :
    num = int(input())
    list.append(num)

x = list[0]
y = list[1]
total = gcd(x, y)

for i in range(2, len(list)) :
    total = gcd(total, list[i])

print("G.C.D is ", total)