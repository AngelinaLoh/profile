# Morse code tutorial

In this tutorial, I will show you how to build a morse code encryption program using Python.

## Prerequisites
install PyCharm, understand basics of Python

## Step by step

1. First create a dictionary with English letters as the keys and the Morse code equivalent as the values.
`morse = {'a': '*---', 'b': '---***', 'c': '---*---*', 'd': '---**', 'e': '*', 'f': '**---*', 'g': '------*',
         'h': '****', 'i': '**', 'j': '*---------', 'k': '---*---', 'l': '*---**', 'm': '------', 'n': '---*',
         'o': '---------', 'p': '*------*', 'q': '-----*---', 'r': '*---*', 's': '***', 't': '---', 'u': '**---',
         'v': '***---', 'w': '*------', 'x': '---**---', 'y': '---*------', 'z': '------**', '1': '*------------',
         '2': '**---------', '3': '***------', '4': '****---', '5': '*****', '6': '---****', '7': '------***',
         '8': '---------**', '9': '------------*', '0': '---------------'}`

2. Create a function for encryption called _encrypt_ with _words_ as the parameter. Create a simple for loop to print the Morse code equivalent for each English letter in _words_ on the same line.
`def encrypt(words):
    for i in words:
        print(morse[i] + ' ', end='')`

3. Create a function for decryption called _decrypt_ with _code_ as the parameter. Set _code_ as plus equal to a string space. Set _decipher_ and _citext_ as blank strings. Then, create a for loop that runs for every character in _code_. Within that for loop, create a if conditional statement that is letter is not a space, set _i_ as 0 and add the character to _citext_. Write else, add 1 to _i_. Within the else statement, if _i_ is equivalent to  2, then add a blank space to _decipher_.  Still within the else statement, create another else statement that sets _dict_index_ as the list conversion of the dictionary values, adds the list conversion of the dictionary keys to _decipher_, and then resets _citext_ and _dict_index_ as blank strings. Finally, after the for loop has finished running, return _decipher_.
`def decrypt(code):
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
    return decipher`

Then,


this is a [hyperlink](https://google.com)

This is a numbered list:
1. yeo
2. whats up
3. b

This is an unordered list:
- ds
- d
- d

this is regular text
`this is code`
