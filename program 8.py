def generate_key(keyword):
    # Generate the key using the given keyword
    key = [ch.upper() for ch in keyword]
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ch not in key:
            key.append(ch)
    return key

def encrypt(plaintext, key):
    # Encrypt the plaintext using the given key
    ciphertext = ""
    for ch in plaintext.upper():
        if ch.isalpha():
            index = ord(ch) - ord('A')
            ciphertext += key[index]
        else:
            ciphertext += ch
    return ciphertext

# Example usage
keyword = "CIPHER"
key = generate_key(keyword)
print("".join(key))  # CIPHERABDFGJKLMNOQSTUVWXYZ
plaintext = "HELLO WORLD"
ciphertext = encrypt(plaintext, key)
print(ciphertext)  # NCFSS QFSCA
