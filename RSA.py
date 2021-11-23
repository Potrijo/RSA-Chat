import rsa
(pubkey, privkey) = rsa.newkeys(512)

'''print(pubkey)
print(privkey)'''
(pubkey, privkey) = rsa.newkeys(512)

print(pubkey)
print(privkey)
'''with open('private.pem', mode='rb') as privatefile:
    keydata = privatefile.read()
privkey = rsa.PrivateKey.load_pkcs1(keydata)'''