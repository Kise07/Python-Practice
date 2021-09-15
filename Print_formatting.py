name = "Kise"
welcome_message = "Hello {} welcome to Python 101".format(name) 

print(welcome_message) # 1


name = "Kise"
welcome_message = "Hello %s welcome to Python 101" % name

print(welcome_message) # 2
name = "Kise"


welcome_message = f"Hello {name} welcome to Python 101" 

print(welcome_message) # 3 modern way, introduce in Python 3.6 v