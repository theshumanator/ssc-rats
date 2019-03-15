from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
print(key)

with open('file_to_encrypt.txt', 'rb') as f:
    data = f.read()

    print(data)

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    print(encrypted)

    with open('file_to_encrypt', 'wb') as f:
        f.write(encrypted)