def my_decorator(func):
    def wrapper():
        print("Do something here")
        func()
        print("Original function is finished")
    return wrapper

@my_decorator   # Just like Inheritance Or extra fuction meaning
def myfunc():
    print("My name is kalob")        

myfunc()    