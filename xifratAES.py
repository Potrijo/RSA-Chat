from Crypto.Cipher import AES
import hashlib


iv = b"1234567890123456"  #16 bytes valor fix
keypass="password entrat per teclat"
misllegitdelarxiu ="Extraterrestres de Raticulin sol·liciten els Plànols del Pentàgon per a invasió imminent"
userName=input("enter user name ")
password=input("enter password")

#HASH
key=password.encode("UTF-8")  #pasem la variable tipus str a bytes
keyhash = hashlib.sha256(key)
print(keyhash)
print("Texto proba1: "+ keyhash.hexdigest())
file=open("text.txt","r")
misllegitdelarxiu = file.read()
file.close()
secret = misllegitdelarxiu.encode("UTF-8")  #pasem la variable tipus str a bytes
#print("MENSAGE SECRETO"+secret)

#XIFRAT
b=keyhash.digest()
f = open(f"pepe.txt", "bw")
f.write(b)
f.close()
print (b)
f = open(f"pepe.txt", "br")
c=f.read()
f.close()
print (c)



#cipher = AES.new(keyhash.digest(), AES.MODE_CFB, iv)
cipher = AES.new(c, AES.MODE_CFB, iv)
encodedtext = cipher.encrypt(secret)
file=open("xifrat.dat", "wb")
file.write(encodedtext)
file.close()


#DESXIFRAT
file=open("xifrat.dat", "rb")
encodedtext = file.read()
cipher = AES.new(keyhash.digest(), AES.MODE_CFB, iv)
decodedtext = (cipher.decrypt(encodedtext))
print (str(decodedtext))  #mostrem la variable com a str