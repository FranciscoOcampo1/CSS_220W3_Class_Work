#Write a Python program to add members to a set.
# Start off with an empty set. Add “Red” to the set.
# Update the set with “Blue” and “Green”.


#create an empty set

colorset = set()
print(colorset)

#Add Blue and Red set
colorset.add("Red")
print("colorset = ", colorset)


#Update the set with Blue and Green
colorset.update(["Blue", "Green"])
print("colorset =", colorset)
