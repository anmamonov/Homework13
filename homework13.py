from enchant.checker import SpellChecker


class CaesarsCipher():

    def __init__(self):
        self.__SYMBOLS = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh'
                          'ijklmnopqrstuvwxyz1234567890 !?.')

    def encrypt(self, msg_cipher, key):
        return str(f'{key}: {self.__cryptographer(msg_cipher, key,
                                                  mode='encrypt')}')

    def decrypt(self, msg_cipher):
        return self.__find_key(msg_cipher, mode='decrypt')

    def decrypt_with_key(self, msg_cipher, key, mode='decrypt'):
        return str(f'{key}: {self.__cryptographer(msg_cipher, key, mode)}')

    def __check_translated_index(self, index, key, mode):
        if mode == 'encrypt':
            return index + key
        elif mode == 'decrypt':
            return index - key

    def __cryptographer(self, msg_cipher, key, mode):
        self.__result_message = ''
        for symbol in msg_cipher:
            index = self.__find_index(symbol)
            if index in range(0, 67):
                translate_index = self.__check_translated_index(index, key,
                                                                mode)
                translate_index = self.__move_pointer(translate_index)
                translate_symbol = self.__SYMBOLS[translate_index]
            else:
                translate_symbol = index
            self.__result_message += translate_symbol
        return self.__result_message

    def __move_pointer(self, index):
        if index >= len(self.__SYMBOLS):
            index = index - len(self.__SYMBOLS)
        elif index < 0:
            index = index + len(self.__SYMBOLS)
        return index

    def __find_key(self, msg_cipher, mode='decrypt'):
        for key in range(0, 26):
            __result_msg = self.__cryptographer(msg_cipher, key, mode)
            if self.__spell_check(__result_msg) is True:
                return str(f'{key}: {__result_msg}')

    def __find_index(self, symbol):
        if symbol in self.__SYMBOLS:
            __index = self.__SYMBOLS.find(symbol)
            return __index
        else:
            return symbol

    def __spell_check(self, msg):
        __checker = SpellChecker("en_US")
        __check_text = msg.split()
        __counter = []
        for i in __check_text:
            __counter.append(__checker.check(i))
        if __counter.count(True) >= __counter.count(False):
            return True


if __name__ == '__main__':
    a = CaesarsCipher()
    path_file: str = input("Путь для сохранения файла"
                           " с результатами шифрования/дешифрования: ")
    with (open(path_file, mode='w', encoding='utf-8', newline='\n')
          as file_write):
        file_write.write(a.decrypt(
            'o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D') + '\n')
        file_write.write(a.encrypt(
            'The password to my mailbox is fBIvqX5yjw', key=21) + '\n')
        file_write.write(a.encrypt(
            'The vacation was a success', key=3) + '\n')
        file_write.write(a.decrypt_with_key(
            'Wkh.ydfdwlrq.zdv.d.vxffhvv', key=3) + '\n')
        file_write.write(a.encrypt(
            'The vacation was a success', key=0) + '\n')
        file_write.write(a.decrypt_with_key(
            'W=kh.ydfdwlrq.zdv.d.vxffhvv', key=3) + '\n')
