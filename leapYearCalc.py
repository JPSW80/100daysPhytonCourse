print("Welcome, user!...This is a Leap Year Calculator")
year = int(input("Tell me what's the year and I will check if it is or not a leap year: "))

if (year%4) != 0:
    print("Not a leap year!")
elif (year%100) != 0:
    print("Leap Year!")
elif (year%400) != 0:
    print("Not a leap year!")
else:
    print("This is a leap year!")

#Another solution:
#if year % 4 ==0:
    #if year%100 ==0:
        #if year%400==0:
            #print("This is a leap year")
        #else:
            #print("Not a leap year")
    #else:
        #print("Leap year")
#else:
    #print("Not a leap year")
