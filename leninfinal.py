#this method will generate a key value which is equal to the length of given string
#if the length of string is greater than length of keyword, keyword will be repeated again
#and again until it matches the string length
#For example, if the input string was 'helloworld' and the key was 'hey', then the key 'hey'
#will be repeated again and again to match length of 'helloworld'. So this method will return
#'heyheyheyh'
def generateKey(string,key):
    #converting key into list of characters
    key=list(key)
    #checking if length of key and string are same
    if len (string)==len(key):
        #no repetitions needed, returning key
        return (key)
    else:
        #continuously appending the key value to itself until it matches the string length
        for i in range(len(string)-len(key)):
            key.append(key[i%len(key)])
    #returning the list of characters combined together as a single string
    return ("".join(key))

#this function generates the encrypted text with the help of the key
def cipherText(string,key):
    #creating an empty list to store cipher text characters
    cipher_text=[]
    #looping from i=0 to i=string length-1
    for i in range (len(string)):
        #the ord method will return the ordinal value of a character. The ordinal value of
        #'A' is 65, that of 'B' is 66, 'C' is 67 etc.
        #so here we find the ordinal value of character at index i in both string and key,
        #find their SUM. The result value is then used in modulo operation with 26, which will
        #return a value between 0 and 25 (which can uniquely refer an alphabet in the english
        # dictionary as in English, there are 26 alphabets)
        x=(ord(string[i])+ord(key[i]))%26
        #as mentioned before, ord('A') is 65, so adding the above value between 0-25 to 'A' will
        #return an alphabet between 'A' and 'Z'
        x+=ord('A')#ord is the returning integer corresponding to uncode
        #appending this ordinal value, converted to corresponding character using chr() method
        #to the cipher text list
        cipher_text.append(chr(x))
    #returning the cipher text list as a single string
    return("".join(cipher_text))

#This function decrypts the encrypted text and returns the original
def originalText (cipher_text,key):
    # creating an empty list to store original text characters
    original_text=[]
    #looping from 0 to cipher text length -1
    for i in range (len(cipher_text)):
        #finding the ordinal value of current cipher character, SUBTRACT the ordinal value of current
        # character at key, and then performed modulo operation with 26 to find a position between
        # 0 and 25
        x=(ord(cipher_text[i])-ord(key[i]))%26
        # adding the ordinal value of 'A' to this value to point to an alphabet
        x+=ord('A')
        #converting to character, appending to original text list
        original_text.append(chr(x))
    #returning original text list as a single string
    return("".join(original_text))

#The driver Code
if __name__ == "__main__":
    #defining a string and keyword
    string=("hellolenin")
    keyword=("hellocopycat")
    #converting both to upper case characters
    string=string.upper() #HELLOLENIN
    keyword=keyword.upper() #CLASSCSI
    #generating key from string and keyword, key will be CLASSCSICL
    key=generateKey(string,keyword)
    #converting to cipher text
    cipher_text=cipherText(string,key)
    #displaying cipher text
    print("Cipher Text is:",cipher_text)
    #converting back to plain text and displaying it
    print("Decrypted text is:", originalText(cipher_text,key))           
