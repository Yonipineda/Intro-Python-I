"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

# YOUR CODE HERE

def combine_12(x, y):
    if type(y) is not int: # check to see if y is an int dtypee
        y = int(y) # if not, y -> int

        return x+y # return combo

print(f'x/y integer: {combine_12(x, y)}') 


# Write a print statement that combines x + y into the string value 57

# YOUR CODE HERE

def combine_57(x, y):
    if type(x) is not str: ## checking to see if x is string, if not
        x = str(x)         ## convert to string

        return x+y         ## return combination 

print(f'x/y string: {combine_57(x, y)}') 