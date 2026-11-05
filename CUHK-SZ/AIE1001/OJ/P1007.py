#Method 1: have a for-loop in another for-loop, means that excecute n**2 times
a = int(input())
letters = input().split()
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for x in alphabet:
    count = 0
    for letter in letters:
        if letter == x:
            count += 1
    print(str(x) + ': ' + str(count))


#Method 2: much more quick, 2n times
n = int(input())
letters = input().split()

count = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
    'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
    'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
    'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
    'Y': 0, 'Z': 0
}

for letter in letters:
    count[letter] += 1

for letter in count:
    print(letter + ": " + str(count[letter]))