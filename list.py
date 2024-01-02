names = ["John", "Adrian", "Mosh", "Mary", "Sam", "Bob"]
names[0] = "Jon"

# Negatives index starts from last index
print(names[-2])

# Selecting a range of values in a list
print(names[0:3])

# List methods
numbers = [1, 2, 3, 4, 5]

# adding a number at the end
numbers.append(6)
print(numbers)

# inserting a number in the middle or beginning
numbers.insert(1, 45)
print(numbers)

# Removing an item
numbers.remove(3)
print(numbers)

# Verifying if a value is in the list  --- in operator
print(1 in numbers)

# Size of the list
print(len(numbers))

# Remove all item --- clear
numbers.clear()

