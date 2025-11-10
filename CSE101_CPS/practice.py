def agez():
    age=int(input("Enter your age:"))
    if age<18:
        if age<13:
            print("Child")
        else:
            print("Teenager")
    elif age<=60:
        print("Adult")
    else:
        print("senior")
    ch=input("do you want to continue,'yes/no'")
    if ch=='yes':
        agez()
    else:
        print("Thank you...")
agez()


