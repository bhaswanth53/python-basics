x = int(input("Please enter a number\n"))
c = []

for i in range(2, (x/2) + 1) :
    if(x % i == 0) :
        c.append(i)

if len(c) == 0 :
    print "Given number is prime"
else :
    print "Given number is not prime"