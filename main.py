num = int(input("Enter the number: "))

print(f"All the factors of {num} are:")
for i in range(1, num+1):
    if num % i == 0:
        print(i)
