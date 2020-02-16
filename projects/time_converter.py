def days_to_hours(days) :
    return days * 24

def days_to_minutes(days) :
    return days_to_hours(days) * 60

def days_to_seconds(days) :
    return days_to_minutes(days) * 60

def hours_to_days(hours) :
    return hours / 24

def hours_to_minutes(hours) :
    return hours * 60

def hours_to_seconds(hours) :
    return hours_to_minutes(hours) * 60

def minutes_to_hours(minutes) :
    return minutes / 60;

def minutes_to_seconds(minutes) :
    return minutes * 60

def minutes_to_days(minutes) :
    return hours_to_days(minutes_to_hours(minutes))

print('Please select the type of number')
print('1 - Days')
print('2 - Hours')
print('3 - Minutes')

num_type = int(input())

print('\nPlease enter the number')

num = int(input())

print('\nPlease select conversion type')
print('1 - Days')
print('2 - Hours')
print('3 - Minutes')
print('4 - Seconds')

con_type = int(input())

if(num_type is 1) :
    if(con_type is 2) :
        print(days_to_hours(num))
    elif(con_type is 3) :
        print(days_to_minutes(num))
    elif(con_type is 4) :
        print(days_to_seconds(num))
    else :
        print('Your selection is invalid')
elif(num_type is 2) :
    if(con_type is 1) :
        print(hours_to_days(num))
    elif(con_type is 3) :
        print(hours_to_minutes(num))
    elif(con_type is 4) :
        print(hours_to_seconds(num))
    else :
        print('Your selection is invalid')
elif(num_type is 3) :
    if(con_type is 1) :
        print(minutes_to_days(num))
    elif(con_type is 2) :
        print(minutes_to_hours(num))
    elif(con_type is 4) :
        print(minutes_to_seconds(num))
    else :
        print('Your selection is invalid')
else :
    print('Your selection is invalid')