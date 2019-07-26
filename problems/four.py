num = int(input("Enter number:\n"))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for i in range(len(a)) :
        if(a[i] < num) :
                """ print a[i]  """
                b.append(a[i])

print b