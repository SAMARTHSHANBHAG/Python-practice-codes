def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
# def factorial(n):: This line defines a function named factorial that takes one argument, n, 
# which represents the number for which we want to calculate the factorial.
# if n == 0:: This line checks if n is equal to 0. If n is indeed 0, it means we've reached the base case of the factorial function (0!), 
# and the function returns 1.
# return 1: This line returns 1 when the base case is reached, i.e., when n is 0. This is because the factorial of 0 is defined as 1.
# else:: If n is not equal to 0, this block of code is executed.
# return n * factorial(n - 1): This line is the recursive step of the factorial function. 
# It calculates the factorial of n by multiplying n with the factorial of n - 1. 
# This process continues recursively until the base case is reached (when n is 0), 
# at which point the recursion stops and the factorial value is calculated by multiplying all the numbers from n down to 1.
    