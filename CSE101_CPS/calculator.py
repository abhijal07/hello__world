def calc():
    n1=float(input("Enter your number:"))
    n2=float(input("Enter the 2nd number:"))
    o=input("enter the arithemetic operator:")
    if o=='+':
        sum=n1+n2
        print(sum)
    elif o=='-':
        diff=n1-n2
        print(difference)
    elif o=='*':
        multiply=n1*n2
        print(multiply)
    elif o=='/':
        division=n1/n2
        print(division)
    else:
        print("invalid")
        calc()      
    x=input("do you want to do  more calculations:-(yes/no)")
    if x=='yes':
        calc()
    else:
        print("bye")
calc()




    
