numbers = list(map(int,input("Enter numbers: ").split()))
odd_numbers=[]
for num in numbers:
    if num%2!=0:
        odd_numbers.append(num)
print("List of odd numbers:",odd_numbers)

