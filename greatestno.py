#condition statement
num1=int(input("enter the num1" " "))
num2=int(input("enter the num2" " "))
num3=int(input("enter the num3" " "))
if num1>num2 and num1>num3:
    print("greatest no is",num1)
elif num2>num1 and num2>num3:
    print("greatest no is",num2)
else:
    print("greatest no is",num3)