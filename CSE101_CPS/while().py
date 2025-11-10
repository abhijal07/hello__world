count=0
while(count<2):
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
    count=count+1
    