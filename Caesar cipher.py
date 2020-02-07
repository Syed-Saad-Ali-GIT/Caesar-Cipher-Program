print("Welcome to Caesar Cipher Program")

print("Would You like to encode or decode [e/d]")


incorrectInput= True

while(incorrectInput):
    userInput = input("[e/d] pick one please :  ")
    if userInput == 'e':
        print("encoding")
        incorrectInput = False
        
    elif userInput == 'd' :
        print("decoding")
        incorrectInput = False

    else : 
        print("error...")
