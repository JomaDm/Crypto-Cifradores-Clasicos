import os


def open_read_file(path):
    file_for_encrypt = open(path, "r", encoding="utf-8")
    return file_for_encrypt.read().replace(" ", "").replace("\n", "").lower()


def write_file(message_encrypt, file_name='encrypted.txt'):
    file_for_decrypt = open(file_name, "w", encoding="utf-8")
    file_for_decrypt.write(message_encrypt)
