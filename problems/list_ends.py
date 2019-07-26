len = int(input("Please enter the length of list:\n"))
lis = []
new = []

for i in range(0, len) :
    x = int(input())
    lis.append(x)

new.append(lis[0])
new.append(lis[::-1][0])

print new