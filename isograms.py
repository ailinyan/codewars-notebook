# PROBLEM DESCRIPTION
# 
# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case

# My naive solution

def is_isogram(string):
    charstring = [char for char in string]
    checked = []
    for char in charstring:
        if char not in checked:
            checked.append(char)
            checked.append(char.upper())
        elif char in checked:
            return False
    return True

# Thoughtful approach

def is_isogram(string):
    return len(string) == len(set(string.lower()))

# What is set() method: https://www.geeksforgeeks.org/python-set-method/

# Kata link: https://www.codewars.com/kata/54ba84be607a92aa900000f1
