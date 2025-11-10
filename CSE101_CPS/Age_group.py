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

