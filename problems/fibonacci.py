def fib(a, b) :
    return a + b

num = int(input("Enter the range of numbers:\n"))

a = 0
b = 1
c = []

for i in range(0, num) :
    if(i == 0) :
        c.append(a)
        c.append(b)
    else :
        c.append(fib(a, b))

    n = a
    a = b
    b = fib(n, b)

print c