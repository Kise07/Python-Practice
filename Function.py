# Example #1
# def somename(name):
#     print(f"Hello {name}")

# somename('Any other name')    # Uses DRY Method (DON'T REPEAT YOURSELF!)

# Example #2
# def somename(name, food):  # example of Tuples
#     print(f"Hello {name}. Let's eat some {food}")

# somename('Kalob', 'tacos')  

# Example #3
# def somename(name, food="Pizza"):  # example of Default Value, if the value is not provided then it will use default value
#     print(f"Hello {name}. Let's eat some {food}")

# somename('Kalob', 'Oranges')  

# # Example #4
# def somename(name, food="Pizza"):  # example of Default Value, if the value is not provided then it will use default value
#     if name.lower() == "kalob":
#         print("Welocme Kalob")

#     print(f"Hello {name}. Let's eat some {food}")

# somename('Kalob', food='Oranges')  


# Example #5
# def somename(name=None, food="Pizza"):  # example of Default Value, if the value is not provided then it will use default value
#     if name is None:
#         name = "Zephyr"

#     person_type = "human"
#     if name == "Zephyr":
#         person_type = "Cat"

#     print(person_type)        
#     print(f"Hello {name}. Let's eat some {food}")

# some_var = somename()  

# print("The variable is ", some_var)

# everything is None default in Python

# def somefunction():
#     return "a value"

# thing = somefunction()    
# print(thing)

def exp(num1, num2):
    total = num1 ** num2
    return total

big_number = exp(33, 6)    
print(big_number)