items = ['One', 'Two', 'Three', 'Four', 'Five'] 

# For Loops:
# for item in items:                        # Continue 
#     if item == 'Two' or item == 'Four':
#         continue

#     print(item)

# for item in items:                     # Break
#     if item == 'Three':
#         break

#     print(item)

# While Loops:                    # Continue 
# num = 0
# while num <= 20:
#     num = num + 1
#     if num % 2 == 0:
#         continue
#     print(num)    


num = 0                             # Break 
while num <= 1_000_000:             # if Pass is ever used it will continue looping & exit it using C
    num = num + 1
    if num == 13:
        break
    print(num)

