num = input("Enter a number: ")
num2 = input("Enter a second number: ")
try:                      # Compulsory run 
    num = int(num)
    num2 = int(num2)
    total = num / num2
except ValueError:        # Value Error detection
    print("Num or num2 were not valid numbers")    
except ZeroDivisionError:  # Zero Division detection
    print("Number ccould not be divided")    
except Exception as e:     # (General error type) Exceptional error or out of concept
    print("Exception was caught")
    print(type(e))