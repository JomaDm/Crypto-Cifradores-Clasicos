
class VigenereCipher():
    alfabetos = {
        'EN': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        'ES': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    }
    alfabeto = []

    def __init__(self):
        print('Initialized Cipher')

    def setAlfabeto(self, Abreviatura_alfabeto='EN'):
        self.alfabeto = self.alfabetos[Abreviatura_alfabeto]

    def createPairs(self, key, msg):
        pairs = []
        lenght_key = len(key)

        # Se generan pares para cifrar [msg,key]
        # HolaHo
        # asdasd
        # [['H','a'],['o','s']]
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
    print(msg)
    encrypted_msg = cipher.encrypt(key, msg)

    print("\n"+encrypted_msg)
    decrypted_msg = cipher.decrypt(key, encrypted_msg)
