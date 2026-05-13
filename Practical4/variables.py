# Store the estimated population of Scotland in millions of people.
a = 5.08  # population in 2004, in millions
b = 5.33  # population in 2014, in millions
c = 5.55  # population in 2024, in millions
# Calculate population changes between the given years.
d = b - a  # change between 2004 and 2014
e = c - b  # change between 2014 and 2024
print("Change from 2004 to 2014:", d, "million")
print("Change from 2014 to 2024:", e, "million")
# Compare d and e.
if d > e:
    print("d is larger than e")
else:
    print("e is larger than d")
# d is larger than e, so population growth is decelerating in Scotland.
# Create two Boolean variables.
X = True
Y = False
# W encodes the Boolean expression "X or Y".
W = X or Y
# Truth table for W = X or Y:
# X      Y      W
# True   True   True
# True   False  True
# False  True   True
# False  False  False
print("X is", X)
print("Y is", Y)
print("W = X or Y is", W)
