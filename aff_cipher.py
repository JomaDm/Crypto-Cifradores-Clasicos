from file_manager import open_read_file, write_file
from validations_aff import validate_key, modinv
import random as rand


class AffineCipher():

    alfabetos = {
        'EN': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        'ES': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    }

    alfabeto = []

    def generateKey(self):
        if self.alfabeto != []:
            alfabeto_length = len(self.alfabeto)
            key_mult = rand.randint(0, alfabeto_length-1)
            while not validate_key(key_mult, alfabeto_length):
                print("Generating key...")
                key_mult = rand.randint(0, alfabeto_length)

            key_acc = rand.randint(1, alfabeto_length)

            return [key_mult, key_acc]
        else:
            print('Alphabet not specified')
            return None

    def setAlfabeto(self, Abreviatura_alfabeto='EN'):
        self.alfabeto = self.alfabetos[Abreviatura_alfabeto]

    def readFile(self, file="message.txt"):
        return open_read_file(file)

    def writeFile(self, encrypted_msg, file="message.aff"):
        write_file(encrypted_msg, file_name=file)

    def validateKey(self, key):
        return validate_key(key, len(self.alfabeto))

    def encrypt(self, keys, message):
        if self.alfabeto != []:
            if self.validateKey(keys[0]):
                mult = keys[0]
                cor = keys[1]

                encrypted = []

                # Obtiene el indice del mensajepi
                for e in message:

                    formula = (mult*(self.alfabeto.index(e)) +
                               cor) % len(self.alfabeto)
                    # para agregar un elemento al final
                    encrypted.append(self.alfabeto[formula])
                    #print ('letra: ',e,EN.index(e))
                # print(encrypted)
                cipher_text = ''.join(encrypted)
                print(cipher_text)
                return cipher_text
            else:
                print('Key not valid')
                return None
        else:
            print('Alphabet not specified')
            return None

    def decrypt(self, keys, ciphertext):
        if self.alfabeto != []:
            mult_in = modinv(keys[0], len(self.alfabeto))
            cor_in = len(self.alfabeto) - keys[1]

            desencrypted = []

            for e in ciphertext:

                formula_inv = (mult_in*(self.alfabeto.index(e)+cor_in)
                               ) % len(self.alfabeto)
                desencrypted.append(self.alfabeto[formula_inv])

            plain_text = ''.join(desencrypted)
            print(plain_text)

            return plain_text
        else:
            print('Alphabet not specified')
            return None


if __name__ == '__main__':
    message = 'holamundo'
    keys = [7, 17]

    cipher = AffineCipher()
    cipher.setAlfabeto('EN')
    keys = cipher.generateKey()
    print(keys)
    encrypted = cipher.encrypt(keys, message)
    decrypted = cipher.decrypt(keys, encrypted)
