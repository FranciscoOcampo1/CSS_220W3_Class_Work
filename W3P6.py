# Write a Python program to check if a set is a subset of another set.
# Use sets x = {apple, mango}, y = {mango, orange},
# and z = {mango}. This program should use the issubset() method.

# Crete sets x, y, and z
x = set(["appkle", "mango"])
y = set(["mange", "orange"])
z = set(["mango"])
print(x)
print(y)
print(z)

# Check for subsets
print("Is x subset of y?")
print(x.issubset(y))

print("Is y subset of x?")
print(y.issubset(x))

print("Is x subset of z?")
print(x.issubset(z))

print("is z subset of x?")
print(z.issubset(x))

print("Is y subset of z?")
print(y.issubset(z))

print("Is z subset of y?")
print(z.issubset(y))