# List Comprehenssion: syntax: [expression for item in iterable if condition == True]
numbers = [1,2,3,4,5,6,7,8,9,10]
square = [i**2 for i in numbers]
print(square)

even_numbers = [i for i in numbers if i%2 == 0]
print(even_numbers)


# flatten a list of lists using list comprehension: Syntax: [item for sublist in list_of_lists for item in sublist]
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
final_list=[ item for sublist in list_of_lists for item in sublist]
print(final_list)

# create a list of tuples using list comprehension: Syntax: [(item1, item2) for item1 in iterable1 for item2 in iterable2]
list1 = [1,2,3]
list2 = ['a','b','c']
tuples_list = [(i, j) for i in list1 for j in list2]
dict_list = [{i:j} for i in list1 for j in list2]
print(tuples_list) #output: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]
print(dict_list) # output: [{1: 'a'}, {1: 'b'}, {1: 'c'}, {2: 'a'}, {2: 'b'}, {2: 'c'}, {3: 'a'}, {3: 'b'}, {3: 'c'}]


# Generate a list of first letters of each word in a list using list comprehension: Syntax: [word[0] for word in words]
words =["apple", "banana", "cherry", "date"]
first_letter =[fruit[0] for fruit in words]
print(first_letter) # output: ['a', 'b', 'c', 'd']

# create a list of squares of even numbers from a list using list comprehension: Syntax: [num**2 for num in numbers if num%2 == 0]
square_of_even_numbers = [num **2 for num in numbers if num % 2 ==0]
print(square_of_even_numbers) #output: [4, 16, 36, 64, 100]

# generate the list of all the divisors of a number using list comprehension: Syntax: [i for i in range(1, num+1) if num % i == 0]
num = 12    
divisors = [i for i in range(1, num +1) if num % i == 0]
print(divisors) # output: [1, 2, 3, 4, 6, 12]

# prime number lst using list comprehension: Syntax: [num for num in range(2, n) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
n = 20
primes = [num for num in range(2, n) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
print(primes) # output: [2, 3, 5, 7, 11, 13, 17, 19]