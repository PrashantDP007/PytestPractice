sum = lambda a, b: a + b
print(sum(5, 10))  # Output: 15

# Lambda function to calculate the square of a number
square = lambda x: x ** 2
print(square(4))  # Output: 16

# return the legth of a string using lambda function
length = lambda s: len(s)
print(length("Hello, World!"))  # Output: 13

#Lambda function to check if a number is even or odd 
is_even = lambda x: x % 2 == 0
print(is_even(4))  # Output: True
print(is_even(5))  # Output: False


# Labmda fucntion to find square of the numbers in a list using map() function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_function = lambda x: x**2
squared_numbers = map(square_function, numbers) # map() syntarx: map(function, iterable)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Labda function to find the even numbers in a list using filter() function
even_function = lambda x: x % 2 == 0
even_numbers = filter(even_function, numbers) # filter() syntax: filter(function, iterable  
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

# sort a list of tuples based on the second element using lambda function
tuples_list = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_tuples = sorted(tuples_list, key=lambda x: x[1]) # sorted() syntax: sorted(iterable, key=function)
print(sorted_tuples)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]

#sort a dictionary based on the values using lambda function
my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1])) # sorted() syntax: sorted(iterable, key=function)
print(sorted_dict)  # Output: {'b': 1, 'c': 2, 'a': 3}  

# Sort a list of strings based on their length using lambda function
strings_list = ['apple', 'banana', 'kiwi', 'cherry']    
sorted_strings = sorted(strings_list, key = lambda x: len(x)) # sorted() syntax: sorted(iterable, key=function)
print(sorted_strings)  # Output: ['kiwi', 'apple', 'banana', 'cherry']

# Sort the list of dictionaries based on the value of a specific key using lambda function
dict_list = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_dict_list = sorted(dict_list, key=lambda x: x['age']) # sorted() syntax: sorted(iterable, key=function)
print(sorted_dict_list)  # Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# Find the maximum value in a dictionary based on the values using lambda function
max_value = max(my_dict.items(), key=lambda item: item[1]) # max() syntax: max(iterable, key=function)
print(max_value)  # Output: ('a', 3)