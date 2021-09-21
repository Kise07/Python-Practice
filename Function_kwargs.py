def person(**kwargs):
    print(kwargs)
    print(type(kwargs))

    if 'age' in kwargs:
        print("You are is", kwargs.get("age"))

person(name="Jacob", age=27, brain="Huge")    