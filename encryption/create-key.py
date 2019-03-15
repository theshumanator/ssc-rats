#this file is not needed in the project

from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)
#write the key to a file to save for future use
file = open('key.key', 'wb')
file.write(key)
file.close()

