print("This is the most accurate tip calculator")

totalBill=input("What was the total bill? AU$")
totalBill=float(totalBill)

percentage=input("What percentage tip you like to give? 10, 12 or 15? AU$")
fpercentage=float(percentage)
percentageTip = (fpercentage/100) #convert % int to float

totalPeople=input("How many people to split the bill? ")
totalPeople=float(totalPeople)

tip=(totalBill*percentageTip/totalPeople)
tipf=round(float(tip),2)

totalBillDiv=((totalBill+(totalBill*percentageTip))/totalPeople)
totalBillDiv=round(totalBillDiv,2)

print(f"Each person should pay: AU${tipf} as tip")
print(f"If  you want to divide the bill in equal part, each one person will pay: AU${totalBillDiv} (including tips)")
