num = int(input("Enter the number of datas: "))

list = []

for i in range(0, num) :
    a, b, c = map(int, input().split())
    x = 0
    if(a**2 + b**2 == c**2) :
        x = 1
    list.append(x)

print(" ". join("{0}".format(n) for n in list))