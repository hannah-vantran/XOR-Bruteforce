#Hannah Vantran
#hannahvantran.com
#11/12/2023

def repeatKey(ciphertext, key):
    repeats = len(ciphertext)//len(key)
    remainder = len(ciphertext) % len(key)
    repeatedKey = ""
    for x in range(repeats):
        repeatedKey += key
    repeatedKey += key[:remainder]
    return repeatedKey

def bruteforce_XOR(ciphertext, known_plaintext):
    #Given ciphertext and known plaintext, bruteforce the key
    b_ct = bytes.fromhex(ciphertext)
    key = "00"
    while 1==1:
        repeatedKey = repeatKey(ciphertext, key)
        b_rk = bytes.fromhex(repeatedKey)
        index = 0
        m = ""
        for byte in b_ct:
            m += chr(byte ^ b_rk[index])
            index += 1
        if m[:len(known_plaintext)] == known_plaintext:
            return m, key
        key = int(key, 16)+1
        key = hex(key)
        key = key[2:]
        if len(key) % 2 != 0:
            key = "0" + key
    return m, key

def main():
    ct = "10580f080f44140f2b130d40520f005019003c2100172117081c"
    k_pt = "s9{"
    message, key = bruteforce_XOR(ct, k_pt)
    print(f'plaintext: {message} key: {key}')
    
main()
