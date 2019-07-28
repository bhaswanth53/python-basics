num = int(input("Enter number of elements: "))
print("Enter Numbers: ")

list = []
sums = []

for i in range(0, num) :
    x, y, z = map(int, input().split())
    list.append(x*y+z)

for i in range(0, len(list)) :
    digits = [int(x) for x in str(list[i])]
    sums.append(sum(digits))

print(" ". join("{0}".format(n) for n in sums))