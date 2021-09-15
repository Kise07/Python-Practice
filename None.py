wallet = None # none = nothing 
#...
# wallet = 82.45 
# # Then we are tend to overwrite it a bit later.

if wallet is None: # "is" "==" used sometime, but alway "is" is used in None Data type.
    print("There nothing in my wallet")
    wallet = 82.45

print("My wallet has ", wallet)    