import os.path
import json

#-------------------------------- CaesarCipher class --------------------------
class  CaesarCipher:
    def __init__(self, key) :
        if key >= 0: 
            key = key % (ord('z') - ord('a'))
        else:
            key = -((-key) % (ord('z') - ord('a')))
        self.key = key

    def encrypt(self, toEncrypt) :
        encryptedWord = ""
        for char in toEncrypt :
            numOfChar = ord(char)
            if char.isalpha():
                if char.isupper():
                    numOfChar = self.getNumOfChar(ord('A') , ord('Z'), numOfChar)
                else:
                    numOfChar = self.getNumOfChar(ord('a') , ord('z'), numOfChar)
            encryptedWord += chr(numOfChar)
        return encryptedWord

    def decrypt(self, toDecrypt) :
        ciphered = CaesarCipher(-(self.key))
        return ciphered.encrypt(toDecrypt)

    def getNumOfChar(self, start, end, numOfChar):
        if (numOfChar + self.key < start):
            numOfChar = end + ((numOfChar + self.key) - start ) +1
        elif (numOfChar + self.key > end):
            numOfChar = start + (self.key - (end -numOfChar)) -1
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
                cipher = CaesarCipher(self.keysList[counter])
                encryptedStr = encryptedStr + cipher.encrypt(char) 
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
                cipher = CaesarCipher(self.keysList[counter])
                decryptedStr = decryptedStr + cipher.decrypt(char)
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
            listOfKeys.append(ord(char) - ord(firstLetter))
    temp_vigener = VigenereCipher(listOfKeys)
    return temp_vigener

def loadEncryptionSystem(dir_path):
    jsonFile = open(dir_path + "//config.json")
    data = json.load(jsonFile)
    type = data['type']
    ifEncrypt = data['encrypt']
    key = data['key']
    jsonFile.close()

    ifKeyIsString = isinstance(key, str)
    if type == 'Vigenere':
        if ifKeyIsString:
            cipher = getVigenereFromStr(key)
        else:
            cipher = VigenereCipher(key)
    else:
        cipher = CaesarCipher(key)
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    #if needs to encrypt .txt files to .enc files
    if ifEncrypt:
        for file in files:
            if file.endswith('.txt'):
                originalFile = open(file, 'r')
                encryptedFileName = os.path.splitext(file)[0] + '.enc'
                encryptedFile = open(encryptedFileName, 'w')
                strForEncrypting = ''
                for line in originalFile:
                    strForEncrypting = strForEncrypting + line
                encryptedFile.write(cipher.encrypt(strForEncrypting))
                originalFile.close()
                encryptedFile.close()
    # if needs to decrypt .enc files to .txt files
    else:
        for file in files:
            if file.endswith('.enc'):
                # fileName = os.path.splitext(os.path.split(txtFile_path)[1])[0]
                originalFile = open(file, 'r')
                decryptedFileName = os.path.splitext(file)[0] + '.txt'
                decryptedFile = open(decryptedFileName, 'w')
                strForDecrypting = ''
                for line in originalFile:
                    strForDecrypting = strForDecrypting + line
                decryptedFile.write(cipher.decrypt(strForDecrypting))
                originalFile.close()
                decryptedFile.close()

