import random
import string

def generate_wordlist(length):
    wordlist = []
    characters = string.ascii_letters + string.digits + "!@#$"
    for _ in range(10000000):
        password = ''.join(random.choice(characters) for _ in range(length))
        wordlist.append(password)
    return wordlist

def save_wordlist(wordlist, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join(wordlist))
    print(f"The list has been saved to file: {filename}")

length = 11  
filename = 'wordlist.txt'

wordlist = generate_wordlist(length)
save_wordlist(wordlist, filename)
