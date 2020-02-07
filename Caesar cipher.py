
textToEncode = ""
deocdedText = ""

textToDecode = ""
encodedText = ""

def encode():
    print("Encoding")
    textToEncode = input("What will you like to encode \n")

    incorrectInput = True
    while(incorrectInput):
        keyShift = input("What do you want the key to be 1-25 \n")
        if(int(keyShift) > 25 or int(keyShift) < 1):
            print("Enter Between 1-25")
        
        else:
            print("Nice Still in Dev... key :" + keyShift)
            incorrectInput = False


def decode(): 
    print("Decoding")
    

print("Welcome to Caesar Cipher Program \n")

print("Would You like to encode or decode [e/d] \n")


incorrectInput= True

while(incorrectInput):
    userInput = input("[e/d] pick one please :  \n")
    if userInput == 'e':
        encode()
        incorrectInput = False
        
    elif userInput == 'd' :
        decode()
        incorrectInput = False

    else : 
        print("error... \n")


