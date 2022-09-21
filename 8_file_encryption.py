infile = open('info_security.txt.', 'r')
infiles = infile.read()
words = infiles.strip()

outfile = open('encrypted.txt', 'w')

codes = {'A': '$', 'a': '9', 'B': '!','b': '1','C': '@',
        'c': '2', 'D': '^^','d': '*', 'E': '<', 'e': '>',
        'F': '?','f': '/','G': 'q', 'g': '|', 'H': '-',
        'h': '~','I': '`', 'i': 'j', 'J': '__','j': 'K','K': '=',
        'k': '{', 'L': '}','l': '[', 'M': ']', 'm': 'n',
        'N': 'w','N': 'W','n': ';', 'O': 'V', 'o': 'v',
        'P': 'r','p': 'R','Q': 't','q': 'T', 'R': 'f', 'r': 'F',
        'S': 'X','s': 'x','T': 'a','t': 'A','u': '3', 'U': '4',
        'V': '5', 'v': '6','W': '7','w': '8','X': '0', 'x': 'd',
        'Y': 'D','y': 'L','Q': 'l','z': '%'}

encrypt = ''
for alph in words:
    if alph in codes:
        encrypt += codes[alph]
    else:
        encrypt += alph

print(encrypt)
outfile.write(encrypt)
outfile.close()
