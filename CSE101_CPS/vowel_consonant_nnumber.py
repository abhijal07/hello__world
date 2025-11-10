str=input("Enter a string")
lst=["a","e","i","o","u"]
for i in str:
    if i in lst:
        print(i," is a vowel")
    elif i.isnumeric():
        print(i," is a number")
    elif i.isalpha():
        print(i," is a consonant") 
    else:
        print(i," is a special character")        
