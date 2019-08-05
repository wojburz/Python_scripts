import math


def Exercise_1(sentence):
    """ 1.	Reverse the order of words in a sentence.
    I.e.: “She sells sea shells” -> “shells sea sells She”.
    Both input and output should be strings."""

    if(isinstance(sentence, str)):
        sentenceWords = list(reversed(sentence.split()))
        result = ""
        for word in sentenceWords:
            result = result + " " + word
        return result[1:]
    else:
        raise ValueError("Enter string as an argument")


def Exercise_2(sentence):
    """2.	Translate input text string to string of numbers on feature-phone keyboard basis.
    I.e. “a” is one press of button 2, “b” - two presses of 2, etc.
    “Eve has a cat”-> 3388833#4427777#2#22228. (One can use # as a space).
    Translation should be case insensitive."""

    if isinstance(sentence, str):
        result = ""
        dictionary = {'a': [1, '2'], 'b': [2, '2'], 'c': [3, '2'],
                      'd': [1, '3'], 'e': [2, '3'], 'f': [3, '3'],
                      'g': [1, '4'], 'h': [2, '4'], 'i': [3, '4'],
                      'j': [1, '5'], 'k': [2, '5'], 'l': [3, '5'],
                      'm': [1, '6'], 'n': [2, '6'], 'o': [3, '6'],
                      'p': [1, '7'], 'q': [2, '7'], 'r': [3, '7'], 's': [4, '7'],
                      't': [1, '8'], 'u': [2, '8'], 'v': [3, '8'],
                      'w': [1, '9'], 'x': [2, '9'], 'y': [3, '9'], 'z': [4, '9'],
                      ' ': [1, '#']}

        for char in sentence:
            if char.lower() in dictionary:
                result += dictionary[char.lower()][0] * dictionary[char.lower()][1]
        return result
    else:
        raise ValueError("Enter string as an argument")


def Exercise_3(number):
    """ 3.	Check how many different digits are in given number. I.e.: 177 - > 2."""
    return len(set(str(number)))

def Exercise_4(txt):
    """ 4.	Palindrome. Write a program which tells if a word or a sentence is a palindrome.
    I.e. “A toyota”, “11 02 2011”, “Anna”. Ignore spaces or letter case."""

    if isinstance(txt, str):
        txtCleared = ""
        for char in txt:
            if char.isalpha():
                txtCleared += char.lower()

        l = len(txtCleared)
        if l % 2 == 0:
            a = txtCleared[:int(l / 2)]
            b = txtCleared[int(l / 2):]
            b = b[::-1]
            if a == b:
                return True
            else:
                return False
        else:
            a = txtCleared[:math.floor(l / 2)]
            b = txtCleared[math.ceil(l / 2):]
            b = b[::-1]
            if a == b:
                return True
            else:
                return False

    else:
        raise ValueError("Enter string as an argument")



#print(Exercise_1("  byłem, dawno tep\mu"))
#print(Exercise_2(43))
#print(Exercise_3(11787))
print(Exercise_4("11 02 A.... 2011"))