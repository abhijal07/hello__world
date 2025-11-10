#gross_bill
price=float(input("Enter the price:"))
total=0
while price!=0:
    total=total+price
    price=float(input("enter the next price,if you are over press 0"))
    print("Total=",total)
