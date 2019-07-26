num = int(input("Enter an integer:\n"))

if(num % 2 == 0) :
    if(num % 4 == 0) :
        print num, " is divisible by 4"
    else :
        print num, " is an even number"
else :
    print num, " is an odd number"