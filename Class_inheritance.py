class Animal:
    fur_color = "Orange"

    def speak(self):
        print("Raawwwrr")

    def eat(self):
        pass

    def chase(self):
        pass

class Tiger(Animal):  # Inheritance using (ClassName)
    pass

tiger = Tiger()
tiger.speak()
print(type(tiger))