list=eval(input("Enter the list: "))
print(list)
for i in range(len(list)):
    lagest=list[0]
    if list[i]>lagest:
        lagest=list[i]
print("Largest element is:",lagest)

