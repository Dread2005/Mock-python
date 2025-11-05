# mock-python: Beginner Exercises
# --------------------------------
# Complete the following functions and class according to the instructions.

# Exercise 1: Add Numbers
"""
Returns the sum of two numbers.

Example:
    add_numbers(2, 3) -> 5
    add_numbers(-1, 4) -> 3
"""
def add_numbers(a, b):
    num_1 = a
    num_2 = b
    return (num_1+num_2)


# Exercise 2: Subtract Numbers
"""
Returns the result of a minus b.

Example:
    subtract_numbers(5, 3) -> 2
    subtract_numbers(3, 5) -> -2
"""
def subtract_numbers(a, b):
    num_1 = a
    num_2 = b
    return (num_1-num_2)


# Exercise 3: FruitLoop
"""
Print numbers from 1 to n, replacing multiples:
- Multiples of 3 -> "Fruit"
- Multiples of 5 -> "Loop"
- Multiples of both 3 and 5 -> "FruitLoop"

Example:
    fruitloop(5) prints:
    1
    2
    Fruit
    4
    Loop
"""
def fruitloop(n):
    value_lst = []
    for value in range(1, n+1):
        if value % 3 == 0 and value % 5 == 0:
            value_lst.append('FruitLoop')
        elif value % 3 == 0:
            value_lst.append('Fruit')
        elif value % 5== 0:
            value_lst.append('Loop')
        else:
            value_lst.append(str(value))
    return value_lst

# Exercise 4: Fibonacci
"""
Returns the nth Fibonacci number (0-indexed: 0,1,1,2,3,5...).

Example:
    fibonacci(5) -> 5
    fibonacci(7) -> 13
"""
# def fibonacci(n: int):
#     value_lst = []
#     current = int
#     for values in range(0, n):
#         value_lst.append(values)
   
#     # while len(value_lst) != 0:
#     #          try:
#     #             current = value_lst[0] + value_lst[1]
#     #             value_lst.pop(0)
#     #         except
    
            
#     print(current)
#     pass
# fibonacci(7)



# Exercise 5: Find Maximum
"""
Returns the largest number in a list.

Example:
    find_max([1,2,3]) -> 3
    find_max([-1,-5,-3]) -> -1
"""
def find_max(numbers: list):
    current_num = numbers[0]
    
    numbers.pop(numbers.index(current_num))

    for values in numbers:
        if values > current_num:
            current_num = values
            continue

    return current_num
   


# Exercise 6: Find Minimum
"""
Returns the smallest number in a list.

Example:
    find_min([1,2,3]) -> 1
    find_min([-1,-5,-3]) -> -5
"""
def find_min(numbers: list):
    current_num = numbers[0]
    
    numbers.pop(numbers.index(current_num))

    for values in numbers:
        if values < current_num:
            current_num = values
            continue

    return current_num
 


# Exercise 7: Person Class
"""
Represents a person with a name and age.

Attributes:
    name (str): Name of the person
    age (int): Age of the person

Method:
    greet() -> "Hello, my name is {name} and I am {age} years old."

Example:
    p = Person("Alice", 25)
    p.greet() -> "Hello, my name is Alice and I am 25 years old."
"""
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hello, my name is {self.name} and I am {str(self.age)} years old'






# Example usage (can be removed or commented out during testing)
# This part is just for demonstration and won't be executed during tests.
# Remove docstrings to see how the functions and class work.
"""
if __name__ == "__main__":
    # Example usage (can be removed or commented out during testing)
    print(add_numbers(2, 3))  # Should print 5
    print(subtract_numbers(5, 3))  # Should print 2
    fruitloop(15)  # Should print numbers and words as per the rules
    print(fibonacci(10))  # Should print 55
    print(find_max([1, 2, 3, 4, 5]))  # Should print 5
    print(find_min([1, 2, 3, 4, 5]))  # Should print 1
    p = Person("Alice", 25)
    print(p.greet())  # Should print greeting message
"""
