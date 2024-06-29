def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1, 3, 5))

# def sum_all(*args):: This line defines a function named sum_all that accepts a variable number of arguments. 
# The *args parameter collects all the positional arguments passed to the function and stores them in a tuple named args.
# print(args): This line prints out the args tuple, showing all the arguments passed to the function.
# for i in args:: This line starts a loop that iterates over each element in the args tuple.
# print(i * 2): Inside the loop, this line prints each element of args multiplied by 2. 
# This demonstrates how you can perform operations on each individual argument passed to the function.
# return sum(args): After the loop, this line calculates the sum of all the elements in the args tuple using the built-in sum() function
#  and returns the result.
# print(sum_all(1, 3, 5)): This line calls the sum_all function with three arguments (1, 3, and 5). The function prints the arguments,
#  prints each argument multiplied by 2, and then returns the sum of all the arguments, which is 1 + 3 + 5 = 9. 
# The final result, 9, is printed to the console by the print statement outside the function call.