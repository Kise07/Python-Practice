# String are un-mutable variables
string = "The fox jumped over the cow" #1 string
string = "Overwritten"                 #2 string 
print(string.upper())                  #Have different memory 
print(string)                          

# List are mutable variables 
names = ['Kalob', 'Jacob', 'Gully', 'Amanda']
names.append('Rubarb')          
print(names)                      