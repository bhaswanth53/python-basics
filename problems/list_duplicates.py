num = int(input("Enter the range of list"))
c = []
for i in range(0, num) :
    x = raw_input("")
    c.append(x)
updated = set(c)
updated = list(updated)
print "Original list is ", c
print "\nUpdated list is ", updated