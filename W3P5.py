# Write a Python program to create set difference.
# Use sets x = {apple, mango} and y = {mango, orange}.


# Create sets x and y
x = set(["apple", "mango"])
y = set(["mango", "orange"])
print(x)
print(y)

# Check for an intersection
a =  x & y
print("Intersection = ", a)

# Set difference of x and y
z = x - y
print("Difference = ", z)
b = y - x
print("Difference = ", b)
c = z | b
print("The real Difference = ", c)