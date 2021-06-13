# PROBLEM DESCRIPTION
# 
#  Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!

n = [1,2,3,4,5,6,7,8,9]
n0, n1, n2, n3, n4, n5, n6, n7, n8 = n
print(n0)
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# Useful links: https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters    

# Kata link: https://www.codewars.com/kata/525f50e3b73515a6db000b83/python