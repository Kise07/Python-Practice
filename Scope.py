# When variable or value is define outside the function it is global but when it's inside the function it only exit in that function

# def myfunc():         # Error Bcuz of the variable is def inside
#     name = "Kalob"

# print(name)    


# Example #2
name = "Kalob"
def myfunc():
    name = "New name" # Overwritting Variable
    return name

print(myfunc())   
print(name) 