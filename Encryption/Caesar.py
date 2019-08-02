import enchant
d = enchant.Dict("en_US")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input('Enter message to be encrypted:\n').lower().strip()
shift = input('Enter shift:\n')


def encrypt():
    ciphertext = ''
    for letter in text:
        num = int(shift) + alphabet.index(letter)
        if num >= 26:
            num -= 26
        ciphertext += alphabet[num]
    return ciphertext


print(encrypt())


def decrypt():
    for i in range(26):
        deciphertext = ''
        for letter in text:
            num2 = alphabet.index(letter) - i
            deciphertext += alphabet[num2]
        if d.check(deciphertext):
            print(deciphertext)


decrypt()
