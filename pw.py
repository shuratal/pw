def vigenere(text: str, key: str, alphabet: str, encrypt):

    result = ""

    for i in range(len(text)):
        letter_n = alphabet.index(text[i])
        key_n = alphabet.index(key[i % len(key)])

        if encrypt:
            value = (letter_n + key_n) % len(alphabet)
        else:
            value = (letter_n - key_n) % len(alphabet)

        result += alphabet[value]

    return result


def vigenere_encrypt(text, key, alphabet):
    return vigenere(text=text, key=key, alphabet=alphabet, encrypt=True)

pw = str(input())
key = str(input())
k2 = 0
letters = ""
digits = ""

for ch in pw:
    if '0' <= ch <= '9':
        digits += ch
    else:
        letters += ch
        
for ch in key:
    k2 += ord(ch)
    

p2 = "".join(sorted(vigenere_encrypt(digits, str(k2), '0123456789')))
p1 = "".join(sorted(vigenere_encrypt(letters, key, 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')))

new_pw = p1 + p2 + "!?"
new_pw[0].upper()

print("\x1b[H\x1b[2J", end="")

print(new_pw + new_pw)
input()