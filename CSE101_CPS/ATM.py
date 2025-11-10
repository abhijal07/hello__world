B=int(input("Enter the balance amount:"))
W=int(input("Enter the withdrawal amount:"))
while W!=0:
    if W<=B:
        B=B-W
        print("Withdrawal sucessfull,Remaining balance:",B)
    else:
        print("insufficient balance")
    W=int(input("Enter the withdrawal amount:"))
print("Final Balance",B)