class Animal:
    fur_color = "Orange"

    def speak(self):       # Not given value
        raise NotImplementedError

    def eat(self):
        pass

    def chase(self):
        pass

class HouseCat(Animal):
    def speak(self):        # Replace the speak
        print("Meeeoowww")

cat = HouseCat()
cat.speak()