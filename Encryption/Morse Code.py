morse = {'a': '*---', 'b': '---***', 'c': '---*---*', 'd': '---**', 'e': '*', 'f': '**---*', 'g': '------*',
         'h': '****', 'i': '**', 'j': '*---------', 'k': '---*---', 'l': '*---**', 'm': '------', 'n': '---*',
         'o': '---------', 'p': '*------*', 'q': '-----*---', 'r': '*---*', 's': '***', 't': '---', 'u': '**---',
         'v': '***---', 'w': '*------', 'x': '---**---', 'y': '---*------', 'z': '------**', '1': '*------------',
         '2': '**---------', '3': '***------', '4': '****---', '5': '*****', '6': '---****', '7': '------***',
         '8': '---------**', '9': '------------*', '0': '---------------'}


def encrypt(words):
    for i in words:
        print(morse[i] + ' ', end='')


def decrypt(code):
    code += ' '

    decipher = ''
    citext = ''
    for letter in code:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                dict_index = list(morse.values()).index(citext)
                decipher += list(morse.keys())[dict_index]
                citext = ''
                dict_index = ''
    return decipher


encrypt((str(input('Type in the message to be translated into morse code\n'))).lower())


decrypted = decrypt(input('Type in the morse code to be translated into English\n'))
print(decrypted)