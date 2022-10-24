print("Welcome to Phyton Pizza  Delivery")
price=0

size=input("What size pizza do you want? S, M or L?")
if size=="S":
    price+=15

elif size=="M":
    price+=20

else:
    price+=25

add_pepperoni=input("Do you want pepperoni in your pizza? Type Y or N: ")
if add_pepperoni =="Y":
    if size=="S":
        price+=2
    else:
        price+=3

X_cheese=input("Do you want Extra cheese? Type Y or N: ")
if X_cheese=="Y":
    price+=1

print(f"Your final cost is AUD${price}")
