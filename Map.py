row1=[1,2,3]
row2=[1,2,3]
row3=[1,2,3]
map=[row1,  row2, row3]
print(f"{row1}\n{row2}\n{row3}")
      
position=input("where should I set the '*' ? Type 1 to 3 for  the horizontal position and 1 to 3 for vertical position" )
horizontal= int(position[0]) #first number
vertical= int(position[1]) #second number

selected_row=map[vertical-1]
selected_row[horizontal-1]="*"


print(f"{row1}\n{row2}\n{row3}")