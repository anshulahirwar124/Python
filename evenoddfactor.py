# Even and Odd factor counting

num = int(input("Enter a number: "))

even_count = 0
odd_count = 0

print("Factors of", num, "are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
        
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print("\nEven factors:", even_count)
print("Odd factors:", odd_count)