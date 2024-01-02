# The Range Function
# We use the range function to generate a sequence of numbers
# 1st arg starting value, second argument ending value and third arg is a step
numbers = range(5, 10, 2)
print(numbers)
for number in numbers:
    print(number)

print("***************************************************")
# we could use the range function directly in the for loop
for item in range(5):
    print(item)
