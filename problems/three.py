check = int(input("Enter check:\n"))
num = int(input("Enter num:\n"))

div = check % num

if(div % 2 == 0) :
    print "Even value"
else :
    print "Odd value"