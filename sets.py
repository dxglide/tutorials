# A Python set is an unordered list of immutable elements. It means:

# Elements in a set are unordered.
# Elements in a set are unique. A set doesn’t allow duplicate elements.
# Elements in a set cannot be changed. For example, they can be numbers, strings, and tuples, but cannot be lists or dictionaries.
# To define a set in Python, you use the curly brace {}. For example:

# skills = {'Python programming','Databases', 'Software design'}


skills = set() # empty set

if not skills:
    print('Empty sets are falsy')

skills = set(['Problem solving','Critical Thinking']) # set with two elements
print(skills)

characters = set('letter') # becauae a string is an iterable, the set() function creates a set of characters from the string 'letter'
print(characters)

ratings = {1, 2, 3, 4, 5}
size = len(ratings) # get the number of elements in the set
print(size)    
print("----  Contains or  not  ---- ")
ratings = {1, 2, 3, 4, 5}
rating = 1
if rating in ratings:
    print(f'The set contains {rating}')
rating = 6
if rating not in ratings:
    print(f'The set does not contain {rating}')

print("----  Adding to set   ---- ")
skills = {'Python programming', 'Software design'}
skills.add('Problem solving')
print(skills)

print("----  Adding to set   ---- ")
skills = {'Problem solving', 'Software design', 'Python programming'}
skills.remove('Software design')
print(skills)

skills = {'Problem solving', 'Software design', 'Python programming'}
if 'Java' in skills:
    skills.remove('Java')

    skills = {'Problem solving', 'Software design', 'Python programming'}
skills.discard('Java')  # raises no error if the element is not in the set


skills = {'Problem solving', 'Software design', 'Python programming'}
skill = skills.pop() # remove and return an arbitrary element from the set
print(skill)

skills = {'Problem solving', 'Software design', 'Python programming'}
skills.clear() # remove all elements from the set
print(skills)

skills = {'Problem solving', 'Software design', 'Python programming'}
skills = frozenset(skills) # create a frozenset from a set

skills = {'Problem solving', 'Software design', 'Python programming'}

for skill in skills:
    print(skill) # loop over the set

skills = {'Problem solving', 'Software design', 'Python programming'}
for index, skill in enumerate(skills):
    print(f"{index}.{skill}") # loop over the set with index



tags = {'Django', 'Pandas', 'Numpy'}
lowercase_tags = {tag.lower() for tag in tags} # create a new set with lowercase tags comprehension
print(lowercase_tags)
tags = {'Django', 'Pandas', 'Numpy'}
new_tags = {tag.lower() for tag in tags if tag != 'Numpy'} # create a new set with lowercase tags comprehension
print(new_tags)

print("----  Set operations: UNION   ---- ")
#The union of two sets returns a new set that contains distinct elements from both sets.

s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}
s = s1.union(s2)
print(s)

s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}
s = s1 | s2    # using the pipe operator
print(s)

print("----  Set operations: method vs. set union operator   ---- ") 
# The union() method vs. set union operator
#However, the union operator (|) only allows sets, not iterables like the union() method.
rates = {1, 2, 3}
ranks = [2, 3, 4]
ratings = rates.union(ranks)
print(ratings)

print("----  Set operations: INTERSECTION   ---- ")
# When intersecting two or more sets, you’ll get a new set consisting of elements that exist in all sets.
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.intersection(s2)
print(s)
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1 & s2
print(s)
numbers = {1, 2, 3}
scores = [2, 3, 4]
numbers = numbers.intersection(scores)
print(numbers)

print("----  Set operations: DIFFERENCE   ---- ")
#The difference between the two sets results in a new set that has elements from the first set 
# which aren’t present in the second set.

s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.difference(s2)
print(s)
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s2.difference(s1)
print(s)
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1 - s2
print(s)
scores = {7, 8, 9}
numbers = [9, 10]
new_scores = scores.difference(numbers)
print(new_scores)

print("----  Set operations: SYMMETRIC DIFFERENCE   ---- ")
# The symmetric difference between two sets is a set of elements that are in either set, but not in their intersection.
# Suppose that you have the following s1 and s2 sets:
# s1 = {'Python', 'Java', 'C++'}
# s2 = {'C#', 'Java', 'C++'}
# The symmetric difference of the s1 and s2 sets returns in the following set:
# {'C#', 'Python'}

s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.symmetric_difference(s2)
print(s)
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1 ^ s2
print(s)
scores = {7, 8, 9}
ratings = [8, 9, 10]
new_set = scores.symmetric_difference(ratings)
print(new_set)

print("----  Set operations: SUBSET   ---- ")
# Introduction to the Python issubset() method
# Suppose that you have two sets A and B.
# Set A is a subset of set B if all elements of A are
# also elements of B. Then, set B is a superset of set A.
# Set A and set B can be equal. If set A and set B are not equal, A is a proper subset of B.
# In Python, you can use the Set issubset() method to check if a set is a subset of another:
#set_a.issubset(set_b)
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
print(scores.issubset(numbers))
numbers = {1, 2, 3, 4, 5}
scores = {5,4, 1, 2, 3}
print(scores.issubset(numbers))
numbers = {1, 2, 3, 4, 5}
scores = {5,4, 1, 2, 3,6}
print(scores.issubset(numbers))

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
result = scores <= numbers
print(result)  # True
result = numbers <= numbers
print(result)  # True

# PROPER  subsset
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
result = scores < numbers
print(result)  # True
result = numbers < numbers
print(result)  # False

print("----  Set operations: SUPERSET   ---- ")
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
result = numbers.issuperset(scores)
print(result)
numbers = {1, 2, 3, 4, 5}
result = numbers.issuperset(numbers) # set is always a superset of itself
print(result)


numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
result = numbers >= scores
print(result)  # True
result = numbers >= numbers
print(result)  # True


print("----  Set operations: DISJOINT   ---- ")
# Two sets are disjoint when they have no elements in common.
# In other words, two disjoint sets are sets whose intersection is an empty set.

odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}
result = odd_numbers.isdisjoint(even_numbers)
print(result)

letters = {'A', 'B', 'C'}
alphanumerics = {'A', 1, 2}
result = letters.isdisjoint(alphanumerics)
print(result)