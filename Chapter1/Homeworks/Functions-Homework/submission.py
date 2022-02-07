# Write a Python function that checks whether a passed string is palindrome or not.
# A palindrome is a word, phrase, or sequence that reads the same backward as forward
def palindrome(s):
    s = s.replace(" ", "")
    return s == s[::-1]

# Write a Python function that takes a number as a parameter and checks if the number is prime or not.
def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Write a Python function to check whether a number is in a given range.
def check_if_n_in_given_range(n, given_range):
    return n in given_range

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Write a Python program to reverse a string.
def reverse_string(s):
    return s[::-1]

# Write a Python function to sum all the numbers in a list
def sum_list(l):
    return sum(l)

# Write a Python function to find the Max of three numbers.
def max_of_three_numbers(a, b, c):
    return max(a, b, c)