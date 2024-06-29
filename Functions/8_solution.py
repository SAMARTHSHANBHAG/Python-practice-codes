def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")

# def print_kwargs(**kwargs):: This line defines a function named print_kwargs that accepts keyword arguments. 
# The **kwargs parameter collects all the keyword arguments passed to the function and stores them in a dictionary named kwargs.
# for key, value in kwargs.items():: This line starts a loop that iterates over each key-value pair in the kwargs dictionary.
# print(f"{key}: {value}"): Inside the loop, this line prints each key-value pair in the format "key: value". 
# This demonstrates how you can access and print individual key-value pairs passed to the function.
# print_kwargs(name="shaktiman", power="lazer"): This line calls the print_kwargs function with two keyword arguments 
# (name="shaktiman" and power="lazer"). The function prints each key-value pair passed as arguments.
# print_kwargs(name="shaktiman"): This line calls the print_kwargs function with one keyword argument (name="shaktiman"). 
# The function prints the single key-value pair passed as an argument.
# print_kwargs(name="shaktiman", power="lazer", enemy="Dr. Jackaal"): This line calls the print_kwargs function with three keyword 
# arguments (name="shaktiman", power="lazer", and enemy="Dr. Jackaal"). The function prints each key-value pair passed as arguments.