#Write a Python program to create an intersection of sets.
# Use sets x = {green, blue} and y = {blue, yellow}.

# Use sets x = (green, blue) and y= (blue,yellow)

x = set(["green", "blue"])
y  = set(["blue", "yellow"])
print(x)
print(y)

# Perform intersection of x and y

z = x & y
print("Intersection = ", z)

