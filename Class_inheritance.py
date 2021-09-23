class Animal:
    fur_color = "Orange"

    def speak(self):
        print("Raawwwrr")

    def eat(self):
        pass

    def chase(self):
        pass

class Tiger(Animal):  # Inheritance using (ClassName)
    def speak(self):
        print("They're GREEEAATTTTT")  #1 Instansiating Or OverWriting

class HouseCat(Animal):

    fur_color = "Black"  #2 Instansiating Or OverWriting
    
    def speak(self):    #3 Instansiating Or OverWriting
        print("Meow")

tiger = Tiger()
tiger.speak()
cat = HouseCat()
cat.speak()
print(cat.fur_color)