from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()

with open('file_to_encrypt', 'rb') as f:
    data = f.read()
    print(data)

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    print(decrypted)


    with open('file_to_encrypt', 'wb') as f:
        f.write(decrypted)