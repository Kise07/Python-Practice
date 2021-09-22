class Animal:
    this_is_a_property = {  # Dictionary
        'key_1': 'value_1'
    }
    this_list = ['Kane', 'Kalob', 'Gully']  # List

    _like_this = "Thsi is aprivate property" # Private in Python

the_animal = Animal()    
# print(the_animal.this_is_a_property) # normal searching
# print(the_animal.this_is_a_property) # normal dictionary searching
# print(the_animal.this_is_a_property['key_1']) # k:v dictionary searching
# print(the_animal.this_list) # normal list searching
# print(the_animal.this_list[2]) # slicing & indexing list

print(Animal.this_list) # In Python, no private/public (DirectClassMethod)