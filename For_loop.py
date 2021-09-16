# fav_foods = ['Pizza', 'Tacos', 'Salmon']  #1 Normal Sentence 

# for food in fav_foods:
#     print(food)

# fav_foods = ['Pizza', 'Tacos', 'Salmon']  #2 Print Formatting

# for food in fav_foods:
#     print(f"My fav food is: {food}")    

# fav_foods = ['Pizza', 'Tacos', 'Salmon']  #3 Comparing 

# for food in fav_foods:
#     if food == "Pizza":
#         size = input("What size pizza would you like? ")
#         print(f"You ordered a {size} pizza")

# fav_foods = ['Pizza', 'Tacos', 'Salmon']  #4 Type Casting
# fav_foods = tuple(fav_foods)

# for food in fav_foods:
#     # if food == "Pizza":
#     #     size = input("What size pizza would you like? ")
#     #     print(f"You ordered a {size} pizza")
#     print(food)

# food = "Pizza!"    #5 looping through String
# for letter in food:
#     print(letter)

person = {      #6 looping through Dictionary
     "name": "Kalob",
     "age": 21,
     "status": "trainee"
}
for key, value in person.items():
    print(f"The key is {key} and the value is {value}")