height= input("What's your height in mitres?: ")
weight= input("What's your weight in Kg?: ")

height=float(height)
weight=float(weight)

BMI = round((weight / (height**2)))

print(f"Your BMI is:  {BMI}")
