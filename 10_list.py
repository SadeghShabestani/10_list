numbers = []
for i in range(3):
    number = int(input("Enter Number: "))
    result = number ** 2
    numbers.append(result)
print(f"Power: {numbers}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
numbers.sort(reverse=True)
print(f"Sort: {numbers}")