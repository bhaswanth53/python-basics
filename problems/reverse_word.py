def reverse(string) :
    string = string.split()
    string = string[::-1]
    string = " ".join(string)
    return string

string = raw_input("Enter a string:\n")

print "The reversed string is \n", reverse(string)