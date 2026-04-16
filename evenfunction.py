def eve_fact(n):
    ans=1
    for i in range(2,n+1,2):
        ans=ans*i
def odd_fact(n):
    ans=1
    for i in range(1,n+1,2):
        ans=ans*i
    return ans
num = int(input("Enter a number: "))
if num % 2 == 0:
     print(eve_fact(num))
else:
    print(odd_fact(num))