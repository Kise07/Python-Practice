class Animal:
    fur_color = "Orange"

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print("I am eating yum yum yum")

    def chase(self, animal="Gazelle"):
        print("I am chasing a", animal)

class HouseCat(Animal):
    def speak(self):
        print("Meeeoowww")

    def eat(self):
        super().eat()                # Bubble-Up the previous eat 
        print("I am eating salmon") 

    def chase(self, animal):
        super().chase(animal)      # moving data around by giving a default
        print(animal, "was caught")       

cat = HouseCat()
cat.chase("mouse")