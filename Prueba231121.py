from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from Crypto.PublicKey import RSA
from random import *
import binascii

def createPublicKey():
    keyP = RSA.generate(2048)
    with open('myPublickey.pem','wb') as fPublic:
        fPublic.write(keyP.export_key('PEM'))
    with open('myPublickey.pem','rb') as fPublic:
        key = RSA.import_key(fPublic.read())
    
    print(str(key))
    return key

def createPrivateKey():
    key = RSA.generate(2048)
    with open('myPrivatekey.pem','wb') as fPrivate:
        fPrivate.write(key.export_key('PEM'))
    
    with open('myPrivatekey.pem','rb') as fPrivate:
        key = RSA.import_key(fPrivate.read())
    return key

def EncodeMessage():

    message = b"Welcome to ins Castellete" 
    key = RSA.importKey(open('myPublickey.pem').read())
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(message)
    print(str(ciphertext))
    with open('encodedMessage.pem', 'wb') as codedFile:
        codedFile.write(ciphertext)
    
    return ciphertext

def DecodeMessage():
    with open('encodedMessage.pem', 'rb') as codedFile:
        encodedMessage = codedFile.read()
        print("\nQuevoyyyyy\n"+str(encodedMessage))
    rsa_key = RSA.importKey(open('myPrivatekey.pem').read())
    privKeyPEM = rsa_key.exportKey()
    print(privKeyPEM.decode('ascii'))
    cipher = PKCS1_OAEP.new(privKeyPEM.decode('ascii'))
    print(str(cipher.decrypt(encodedMessage)))

    
EncodeMessage()
DecodeMessage()

