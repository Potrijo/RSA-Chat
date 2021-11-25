from Crypto.PublicKey import RSA

gen_pub_key = RSA.generate(2048).public_key()
gen_priv_key = RSA.generate(2048)

pubkey_file = open('pubkey.pem','wb')
pubkey_file.write(gen_pub_key.export_key('PEM'))
pubkey_file.close()

privkey_file = open('privkey.pem','wb')
privkey_file.write(gen_priv_key.export_key('PEM'))
privkey_file.close()


read_public_key = open('pubkey.pem','r')
pubkey = RSA.import_key(read_public_key.read())

read_private_key = open('privkey.pem','r')
privkey = RSA.import_key(read_private_key.read())

print(privkey)
print(pubkey)