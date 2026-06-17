# Linear Search Program

# Get list elements from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Element to search
key = int(input("Enter the number to search: "))

# Linear Search
found = False

for i in range(len(numbers)):
    if numbers[i] == key:
        print(f"Element found at index {i}")
        found = True
        break

if not found:
    print("Element not found")