import sys

def find_numerals(s):
    numeral_map = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    numerals = []
    word = ''
    for char in s:
        if char.isalpha():
            word += char
        else:
            if word:
                numerals.append(numeral_map.get(word, ''))
                word = ''
    return ''.join(sorted(numerals))

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    for line in lines:
        line = line.strip()
        result = find_numerals(line)
        print(result)
