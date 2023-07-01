class  CaesarCipher:
    def __init__(self, key) :
        self.key = key
    
    def encrypt(self, toEncrypt) :
        encryptedWord = ""
        numOfChar = ord(char)
        for char in toEncrypt :
            if(char >= 'A' and char <= 'Z'): 
                numOfChar = self.getNumOfChar(ord('A') , ord('Z'), numOfChar)   
            elif (char >= 'a' and char <= 'z') :
                numOfChar = self.getNumOfChar(ord('a') , ord('z'), numOfChar) 
            encryptedWord += chr(numOfChar)
        return encryptedWord
    
    def decrypt(self, toDecrypt) :
        ciphered = CaesarCipher(-(self.key))
        return ciphered.encrypt(toDecrypt)
    
    def getNumOfChar(self, start, end, numOfChar):
        if (numOfChar + self.key < start):
            numOfChar = end + ((numOfChar + self.key) - start)
        elif (numOfChar + self.key > end):
            numOfChar = start + ((numOfChar + self.key) - end)
        else :
            numOfChar = numOfChar + self.key
        return numOfChar