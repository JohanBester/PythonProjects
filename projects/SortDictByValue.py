"""
How to Sort a Dictionary by Value in Python
--------------------------------------------
Python doesn’t have an inbuilt method to do this.
The sorted() method sorts iterable data such as lists, tuples, and dictionaries. 
-- But it sorts by key only.
-- The sorted() method puts the sorted items in a list. 

The challenge is to sort by value and maintain a dictionary after the fact.
To correctly sort a dictionary by value with the sorted() method, 
you will have to do the following:
-- pass the dictionary to the sorted() method as the first value
-- use the items() method on the dictionary to retrieve its keys and values
-- write a lambda function to get the values retrieved with the item() method
-- convert the resulting list to a dictionary with dict() method

Using a dictionary of footballers and their total goals scored

"""
footballers_goals = {
    "Eusebio": 120,
    "Cruyff": 104,
    "Pele": 150,
    "Ronaldo": 132,
    "Messi": 125,
}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x: x[1])
# to get the values of the dict, we use 1 in the lambda function.
# 1 represents the indexes of the values. The keys are 0.

print("\n'sorted_footballers_by_goals' ... \n", sorted_footballers_by_goals)
# Output:[('Cruyff', 104), ('Eusebio', 120), ('Messi', 125), ('Ronaldo', 132), ('Pele', 150)]

"""
The problem is that the dictionary is not a dictionary anymore.
The individual keys and values were put in tuples, into a list.
To convert the resulting list to a dictionary, 
just pass the variable of the list into the dict() method.
"""
converted_dict = dict(sorted_footballers_by_goals)
print("\n 'converted_dict' ... \n", converted_dict)
# Output: {'Cruyff': 104, 'Eusebio': 120, 'Messi': 125, 'Ronaldo': 132, 'Pele': 150}

# We sorted the values in a dictionary and convert back to a dictionary
