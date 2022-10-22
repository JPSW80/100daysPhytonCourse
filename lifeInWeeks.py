print("WARNING!\n")
print("This may change your life")
curAge=input("What's your current age? ")

#daysLeft = int(((365*90) - (365*int(curAge)))) #years left in days
#weeksleft=(daysLeft//7)
#monthsleft=(daysLeft//31)

totaldaysLeft =90-int(curAge)
totaldaysLeft=int(totaldaysLeft)
daysLeft=totaldaysLeft*365
weeksleft=totaldaysLeft*52
months=totaldaysLeft*12
print(f"You have a remaining of {daysLeft} days, {weeksleft} weeks or {months} months left")
