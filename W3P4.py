# Write a Python program to create a union of sets.
# Use sets x = {green, blue} and y = {blue, yellow}.



# Create sets x and y

x = set(["green", "blue"])
y = set(["blue", "yellow"])
print(x)
print(y)

# Perform union
z = x | y
print("union = ", z)