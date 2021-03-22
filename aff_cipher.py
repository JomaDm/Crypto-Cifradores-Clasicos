from file_manager import *


n = {'EN': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
     'ES': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
     }


def encrypt(EN, key, message):
    mult = key[0]
    cor = key[1]

    encrypted = []

    # Obtiene el indice del mensaje
    for e in message:

        formula = (mult*(EN.index(e)) + cor) % len(EN)
        encrypted.append(EN[formula])  # para agregar un elemento al final
        #print ('letra: ',e,EN.index(e))
    # print(encrypted)
    cipher_text = ''.join(encrypted)

    write_file(cipher_text, file_name='encrypted_aff.txt')


def decrypt(EN, key_inv, ciphertext):

    mult_in = key_inv[0]
    cor_in = key_inv[1]

    desencrypted = []

    for e in ciphertext:

        formula_inv = (mult_in*(EN.index(e)+cor_in)) % len(EN)
        desencrypted.append(EN[formula_inv])

    #print (''.join(desencrypted))
    plain_text = ''.join(desencrypted)
    write_file(plain_text, file_name='decrypted_aff.txt')


if __name__ == '__main__':
    message = 'holamundo'
    encrypt(n['EN'], [7, 17], message)
    decrypt(n['EN'], [15, 9], 'olqrxbeml')
