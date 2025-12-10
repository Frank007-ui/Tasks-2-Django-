numbers = [10, 29, 5, 87, 3, 50]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest number:", largest)
