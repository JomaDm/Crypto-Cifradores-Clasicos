import os

def open_read_file(path):
    file_for_encrypt = open(path)
    return file_for_encrypt.read()

def write_file(message_encrypt,file_name = 'encrypted.txt'):
    file_for_decrypt = open(file_name, "w")
    file_for_decrypt.write(message_encrypt)
