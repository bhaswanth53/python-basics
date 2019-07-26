""" Number = int(input("\nPlease Enter the Range Number: "))

i = 0
First_Value = 0
Second_Value = 1

while(i < Number):
        if(i <= 1):
            Next = i
        else :
            Next = First_Value + Second_Value
            First_Value = Second_Value
            Second_Value = Next
        print(Next)
        i = i + 1 """

number = int(input("Please enter the range: \n"))

a = 0
b = 1

count = 0

while(count < number) :
    if(count <= 1) :
        num = count
    else :
        num = a + b
        a = b
        b = num
    print num
    count = count + 1