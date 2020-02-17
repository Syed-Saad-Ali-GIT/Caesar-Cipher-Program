import os.path

textToEncode = ""

textToDecode = ""

# Encoduing function
# Asks for user inputs - the text to encode and the key shift
# Encodes the text and saves it to a file
# currently encodes and prints to console - no file saving implemented yet


def encode():
    incorrectInput = True
    print("Encoding \n")

    # Loops until a only alphabetical texts are given
    while(incorrectInput):
        textToEncode = input("What will you like to encode \n")
        if(textToEncode.isalpha()):
            incorrectInput = False
        else:
            print("Enter Only Alphabets , no numbers or special characters \n")

    incorrectInput = True
    # loop until a proper shift key between 1-25 is given
    while(incorrectInput):
        try:
            keyShift = input("What do you want the key to be 1-25 \n")
            if(int(keyShift) > 25 or int(keyShift) < 1):
                print("Enter Between 1-25")

            else:
                incorrectInput = False
        except:
            print("Something Went Wrong :( \n")

    # Main algorithm for Caesar Shift Encoding
    currentLetter = 0
    originalShift = int(keyShift)
    for x in textToEncode:
        keyShift = originalShift
        # Checks if shift will reset to "a" or not
        # if it does it changes the keyshift accordingly
        if(ord(x) + int(keyShift) > ord("z")):
            keyShift = int(keyShift) - (ord("z") - ord(x) + 1)
            x = "a"

        # Changes the text to the encoded message
        textToEncode = textToEncode[:currentLetter] + \
            (chr(ord(x)+int(keyShift))) + textToEncode[currentLetter+1:]
        currentLetter += 1

    # currently only printing to console
    print(textToEncode + "\n")

    #File Writting

    print("Writting to file...")
    f = open("Encoded_Message.txt", "w")
    f.write(textToEncode)
    f.close()


# Function Respoinsible for decoding the encrpyted text
# Load txt file and get decoded message printed onto console
def decode():
    print("Decoding \n")
    incorrectInput = True
    fileMissing = True
    fileName = ""

    #Loops Until user enters correct file with proper format
    while(incorrectInput):
        fileName = input("Enter File Name with Message [.txt] \n")
        while(fileMissing):
            if(os.path.isfile(fileName + ".txt")):
                print("File Does Exist \n")
                fileMissing = False
            else:
                print("File Missing \n") 
       
        f = open(fileName+".txt" ,"r")
        textToDecode = f.readline()

        #Checks if content is only alphabet
        if(textToDecode.isalpha()):
            incorrectInput = False
            f.close()
        else: 
            print("Error in file content only alphabetical characters \n")
    
    incorrectInput = True
    # loop until a proper shift key between 1-25 is given
    while(incorrectInput):
        try:
            keyShift = input("What do is the key? [1-25] \n")
            if(int(keyShift) > 25 or int(keyShift) < 1):
                print("Enter Between 1-25")

            else:
                incorrectInput = False
        except:
            print("Something Went Wrong :( \n")

    # Main algorithm for Caesar Shift Decoding
    currentLetter = 0
    originalShift = int(keyShift)
    for x in textToDecode:
        keyShift = originalShift
        # Checks if shift will reset to "a" or not
        # if it does it changes the keyshift accordingly
        if(ord(x)-int(keyShift) < ord("a")):
            keyShift = (ord("a")-ord(x)-1) + int(keyShift)
            x = "z"

        # Changes the text to the decoded message
        textToDecode = textToDecode[:currentLetter] + \
            (chr(ord(x)-int(keyShift))) + textToDecode[currentLetter+1:]
        currentLetter += 1

    # currently only printing to console
    print(textToDecode + "\n")
    #File Writting

    print("Writting to file...")
    f = open("Decoded_Message.txt", "w")
    f.write("Message : " + textToDecode)
    f.close()

# Basic Program load
print("Welcome to Caesar Cipher Program \n")

print("Would You like to encode or decode [e/d] \n")


incorrectInput = True
# User input menu , makes sure user picks correct options
while(incorrectInput):
    userInput = input("[e/d] pick one please :  \n")
    if userInput == 'e':
        encode()
        incorrectInput = False

    elif userInput == 'd':
        decode()
        incorrectInput = False

    else:
        print("error... \n")
