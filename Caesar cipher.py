
textToEncode = ""
deocdedText = ""

textToDecode = ""
encodedText = ""

def encode():
    incorrectInput = True
    print("Encoding")


    while(incorrectInput):
        textToEncode = input("What will you like to encode \n")
        if(textToDecode.isalpha):
            incorrectInput=False
        else:
            print("Enter Only Alphabets , no numbers or special characters")

            
    incorrectInput = True       
    while(incorrectInput):
        try:
            keyShift = input("What do you want the key to be 1-25 \n")
            if(int(keyShift) > 25 or int(keyShift) < 1):
                print("Enter Between 1-25")
            
            else:
                print("Nice Still in Dev... key :" + keyShift + "\n")
                print(textToEncode)
                textToDecode
                incorrectInput = False
        except:
            print("Something Went Wrong :( \n")


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


