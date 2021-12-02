import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.Cipher import PKCS1_OAEP

# Crea clau privada i l'arxiu myPrivateKey.pem
def generatePrivateKey():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator) #generate pub and priv key
    with open('myPrivatekey.pem','wb') as fPrivate:
        fPrivate.write(key.export_key('PEM'))
    return key

# Llegeix l'arxiu que conté la clau privada
def readMyPrivateKey(key):
    with open('myPrivatekey.pem','rb') as fPrivate:
        key = RSA.import_key(fPrivate.read())
    return key

# Crea clau privada i l'arxiu myPrivateKey.pem
def createPublicKey(key):
    publickey = key.publickey() # pub key export for exchange
    with open('myPublickey.pem','wb') as fPublic:
        fPublic.write(key.export_key('PEM'))
    return publickey

# Llegeix l'arxiu que conté la clau publica
def readPublicKey(key):
    with open('myPublickey.pem','rb') as fPublic:
        key = RSA.import_key(fPublic.read())
    return key

#message to encrypt is in the above line 'encrypt this message'
def encryptMessage(publickey):
    encryptor = PKCS1_OAEP.new(publickey)
    encrypted = encryptor.encrypt(b'encrypt this message')

    print('encrypted message:', encrypted) #ciphertext
    f = open ('encryption.txt', 'w')
    f.write(str(encrypted)) #write ciphertext to file
    f.close()

    return encrypted



#decrypted code below

def decrypted(key, encrypted):

    f = open('encryption.txt', 'r')
    message = f.read()

    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))

    print('decrypted', decrypted)

    f = open ('encryption.txt', 'w')
    f.write(str(message))
    f.write(str(decrypted))
    f.close()
    
    return decrypted

def demo():
    key = generatePrivateKey()
    print(readMyPrivateKey(key))
    publickey = createPublicKey(key.public_key())
    print(readPublicKey(key))
    mEncrypted = encryptMessage(publickey)
    decryptMessage = decrypted(key, mEncrypted)
    print(str(decryptMessage))

demo()

