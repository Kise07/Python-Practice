names = [("name", "Kalob"), ("occupation", "Coder")]

# Simple & long 
d = {}
for key, value in names:
    d[key] = value
print(d)    
print(type(d))


# Simple & short
d = {key: value for key, value in names}
print(d)

# Simplest & modern way
d = dict(names)
print(d)