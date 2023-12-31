translateDict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.' : '.-.-.-',
    ',' : '--..--',
    '?' : '..--..',
    "'" : '.---.',
    '!' : '-.-.--',
    '/' : '-..-.',
    '(' : '-.--.',
    ')' : '-.--.-',
    '&' : '.-...',
    ':' : '---...',
    ';' : '-.-.-.',
    '=' : '-...-',
    '+' : '.-.-.',
    '-' : '-....-',
    '_' : '..--.-',
    '"' : '.-..-.',
    '$' : '...-..-',
    '@' : '.--.-.'
}


def translate(message, flag):
    translatedMessage = ''
    if (flag == 1):
        reversedDict = {value: key for key,value in translateDict.items()}
        tempChar = ''
        for char in message:
            if (char == ' ' and tempChar != ''):
                if(reversedDict[tempChar.strip()] != 'fullstop'):
                    translatedMessage += reversedDict[tempChar.strip()]
                tempChar = ''
                continue
            elif (char == '/'):
                translatedMessage += ' '
                continue
            tempChar += char
        if(tempChar and reversedDict[tempChar.strip()] != 'fullstop'):
            translatedMessage += reversedDict[tempChar.strip()]

    else:
        for char in message:
            if (char == ' '):
                translatedMessage += '/ '
                continue
            translatedMessage += translateDict[char.upper()] + ' '
    
    return translatedMessage


if __name__ == '__main__':
    toFrom = False
    while (toFrom != 1 and toFrom != 2):
        if (toFrom):
            print('\nInvalid input, please enter a valid input.') 
        try:
            toFrom = int(input('Enter 1 for Morse Code --> English, or 2 for English --> Morse Code\n > '))
        except ValueError:
            pass
    
    message = input('Input message:\n > ')

    newText = translate(message, toFrom)

    print('Translated Text:\n' + newText)