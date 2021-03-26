from file_manager import open_read_file, write_file
import random as rand


class VigenereCipher():
    alfabetos = {
        'EN': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '\n'],
        'ES': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '\n'],
        'ASCII': [str(chr(i)) for i in range(256)]
    }
    alfabeto = []

    def __init__(self):
        print('Initialized Vigenere Cipher')

    def generateKey(self, length=10):
        if self.alfabeto != []:
            key = ""
            for _ in range(length):
                key += self.alfabeto[rand.randint(0, len(self.alfabeto)-1)]
            return key
        else:
            print('Alphabet not specified')
            return None

    def setAlfabeto(self, Abreviatura_alfabeto='EN'):
        self.alfabeto = self.alfabetos[Abreviatura_alfabeto]

    def readFile(self, file="message.txt"):
        return open_read_file(file)

    def writeFile(self, encrypted_msg, file="message.vig"):
        write_file(encrypted_msg, file_name=file)

    def createPairs(self, key, msg):
        pairs = []
        lenght_key = len(key)

        # Se generan pares para cifrar [msg,key]
        # HolaHo
        # asdasd
        # [['H','a'],['o','s']] ...
        for i, e in enumerate(msg):
            pairs.append([e, key[i % lenght_key]])

        return pairs

    def encrypt(self, key, msg):
        if(self.alfabeto != []):
            pairs = self.createPairs(key, msg)
            lenght_alf = len(self.alfabeto)

            encrypted = []
            for i in pairs:
                pair = i
                index_y = self.alfabeto.index(pair[1])
                index_x = self.alfabeto.index(pair[0])
                encrypted.append(self.alfabeto[(index_y+index_x) % lenght_alf])
            print("".join(encrypted))
            return "".join(encrypted)
        else:
            print('Alphabet not specified')
            return None

    def decrypt(self, key, c_msg):
        if(self.alfabeto != []):
            lenght_alf = len(self.alfabeto)
            pairs = self.createPairs(key, c_msg)

            decrypted = []
            for i in pairs:
                pair = i
                index_y = self.alfabeto.index(pair[1])
                index_x = self.alfabeto.index(pair[0])
                decrypted.append(
                    self.alfabeto[(index_x+(lenght_alf-index_y)) % lenght_alf]
                )
            print("".join(decrypted))
            return "".join(decrypted)

        else:
            print('Alphabet not specified')
            return None


if __name__ == '__main__':
    cipher = VigenereCipher()
    cipher.setAlfabeto('EN')

    msg = 'denialofservice'
    key = 'forget'
    print(cipher.generateKey())

    print(msg)
    encrypted_msg = cipher.encrypt(key, msg)

    print("\n"+encrypted_msg)
    decrypted_msg = cipher.decrypt(key, encrypted_msg)
