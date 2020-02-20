
# Caesar cipher 


## About
Implement a Caesar cipher, both encoding and decoding. The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC". This simple "monoalphabetic substitution cipher" provides almost no security, because an attacker who has the encoded message can either use frequency analysis to guess the key, or just try all 25 keys.


## Encoding Function

1. Enter a message to encode (only alphabets and no space)
2. Enter a key [1-25]
3. Saves Encoded Message to file "Encoded_Message.txt"

## Decoding Function

1. Enter file with correct formatt and message
2. Enter key shift [1-25]
3. Saves Decoded messafe to file "Decoded_Message.txt"

## File Format For Decoding

When using a personal file for decoding a message the following must be followed :
- single line file with message
- message only has characters (No space , no numbers or symbols)
- The file is in .txt format

## Future Plan 

- MVC GUI
- Allow more file types 
- More Error handling
- Better Algorithm
- Newer encoding algorithms (RSA etc)

