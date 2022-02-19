from doctest import debug_script
import random
import string
#takes file then converts it into a string function
#main function to call other functions
def main():
    
    usertext = int(input(" 0 for encipher 1 for decipher "))
    if usertext == 0:
            encip=readfile("Insert text file name here:")
            gplen = len(encip)
            otp = generatePad(gplen)
            
            encrpyted = encipher(encip, otp)
            print("Encrypted text here:", encrpyted)
            print("One time pad:",otp)
    elif usertext==1:
            decip=readfile("Insert one time pad:")
           
            deciph=readfile("Insert text file name here:")
    
            decrypt=decipher(deciph,decip)
            print("Message:",decrypt)

def readfile(prompt):
    txt=input(prompt)
    f=open(txt,"r")
    txtread=f.read()
    f.close()
    return txtread

    

# Shift a letter by the designated amount, regardless of case
#encipher process
def shiftLetter(char, shift):
    # Get the ASCII number for the character
    ascii = ord(char)
    # If the ASCII code is an uppercase letter,
    # Shift and unshift by 65 so A=0 and Z=25
    if (ascii >= 65) and (ascii <= 90):
        shifted = (ascii - 65 + shift) % 26 + 65
    # If the ASCII code is a lowercase letter,
    # Shift an unshift by 97 so a=0 and z=25
    elif (ascii >= 97) and (ascii <= 122):
        shifted = (ascii - 97 + shift) % 26 + 97
    # If the ASCII code isn't a letter,
    # Don't shift it at all
    else:
        shifted = ascii
    # Return the shifted ASCII code as a character
    return chr(shifted)

#generate pad function to make 
def generatePad(lengp):
   
    upperran = string.ascii_uppercase
    otp = ''.join(random.choice(upperran) for i in range(lengp)) 
    #print("One time pad from encipher",otp)
    return otp 

 
#take a length in characters as input ans create a 
#one tine pad file of random 


#function to encipher text input
def encipher(encip, otp):

    Convertlist = []
    strc = ""
    padindex = 0
 
    for i in range(len(encip)):
        char = encip[i]
        #pad = otp[i]
        #convert = shiftLetter(char, ord(pad)-65) 
        asci=ord(char)
        #can be subject to change to do the inverse for decipher
       
        if (asci>=65 and asci<=90) or (asci>=97 and asci<=122):
            key = otp[padindex]
            encip = shiftLetter(char,ord(key)-65)#shift input change; work back from the real number
            Convertlist.append(encip)
            padindex = padindex +1
        else:
             Convertlist.append(encip)
    return(strc.join(Convertlist))   

#function to decipher text input 
def decipher(deciph, otp):

    decriptlist = []
    strd = ""
    padindex = 0
    # pad index 
    for i in range(len(deciph)):
        char = deciph[i]
        asci = ord(char)
        
        if (asci>=65 and asci<=90) or (asci>=97 and asci<=122):
            key = otp[padindex]
            deci = shiftLetter(char, -ord(key)-65)#shift inpit change; work back from the real number
            decriptlist.append(deci)
            padindex = padindex +1
        else:
            decriptlist.append(char)
  
    return (strd.join(decriptlist))



if __name__ == "__main__":
    main()
