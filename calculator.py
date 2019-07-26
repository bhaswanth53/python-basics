def sum(a, b) :
    return a + b

def sub(a, b) :
    return a - b

def mult(a, b) :
    return a * b

def div(a, b) :
    return a / b

def mod(a, b) :
    return a % b 

a = int(input("Enter first integer: \n"))
b = int(input("Enter second integer: \n"))

print("1. Sum")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus\n")

act = int(input("Enter the type of action:\n"))

if(act == 1) :
    print 'sum is', sum(a, b)

elif(act == 2) :
    print 'sub is', sub(a, b)

elif(act == 3) :
    print 'mult is', mult(a, b)

elif(act == 4) :
    print 'div is', div(a, b)

elif(act == 5) :
    print 'mod is',mod(a, b)
else :
    print "Invalid selection"

