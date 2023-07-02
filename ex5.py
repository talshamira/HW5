#-------------------------------- Helper Functions --------------------------
# returns encrypted letter
def encryptCharacter(charToEncrypt, key):
    if not charToEncrypt.isalpha():
        return charToEncrypt
    finalLetter = 'Z'
    firstLetter = 'A'
    if charToEncrypt.islower():
        finalLetter = 'z'
        firstLetter = 'a'
    if ord(charToEncrypt) + key > ord(finalLetter):
        keyLeftToAdd = key - (ord(finalLetter) - ord(charToEncrypt))
        return chr(ord(firstLetter) + keyLeftToAdd - 1)
    elif ord(charToEncrypt) + key < ord(firstLetter):
        keyLeftToDiff = key + (ord(charToEncrypt) - ord(firstLetter)) + 1
        return chr(ord(finalLetter) + keyLeftToDiff)
    else:
        return chr(ord(charToEncrypt) + key)


# returns decrypted letter
def decryptCharacter(charToDecrypt, key):
    if not charToDecrypt.isalpha():
        return charToDecrypt
    finalLetter = 'Z'
    firstLetter = 'A'
    if charToDecrypt.islower():
        finalLetter = 'z'
        firstLetter = 'a'
    if ord(charToDecrypt) - key > ord(finalLetter):
        keyLeftToAdd = key + (ord(finalLetter) - ord(charToDecrypt))
        return chr(ord(firstLetter) - keyLeftToAdd - 1)
    elif ord(charToDecrypt) - key < ord(firstLetter):
        keyLeftToDiff = key - (ord(charToDecrypt) - ord(firstLetter)) - 1
        return chr(ord(finalLetter) - keyLeftToDiff)
    else:
        return chr(ord(charToDecrypt) - key)


#-------------------------------- CaesarCipher class --------------------------
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


#-------------------------------- VigenereCipher class --------------------------
class VigenereCipher:
    def __init__(self, numbersList):
        self.keysList = numbersList.copy()

    def encrypt(self, strToEncrypt):
        lenOfKeyList = len(self.keysList)
        counter = 0
        encryptedStr = ''
        for char in strToEncrypt:
            if counter == lenOfKeyList:
                counter = 0
            if char.isalpha():
                encryptedStr = encryptedStr + encryptCharacter(char, self.keysList[counter])
                counter = counter + 1
            else:
                encryptedStr = encryptedStr + char
        return encryptedStr

    def decrypt(self, strToDecrypt):
        lenOfKeyList = len(self.keysList)
        counter = 0
        decryptedStr = ''
        for char in strToDecrypt:
            if counter == lenOfKeyList:
                counter = 0
            if char.isalpha():
                decryptedStr = decryptedStr + decryptCharacter(char, self.keysList[counter])
                counter = counter + 1
            else:
                decryptedStr = decryptedStr + char
        return decryptedStr


#-------------------------------- External Functions --------------------------
def getVigenereFromStr(inputStr):
    listOfKeys = []
    firstLetter = ''
    for char in inputStr:
        if char.isalpha():
            if char.islower():
                firstLetter = 'a'
            else:
                firstLetter = 'A'
            print(firstLetter)
            listOfKeys.append(ord(char) - ord(firstLetter))
    temp_vigener = VigenereCipher(listOfKeys)
    return temp_vigener;

#def loadEncryptionSystem(dir_path):
