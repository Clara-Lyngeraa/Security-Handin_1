import random

g = 666
p = 6661
PK = 2227
m = 2000

def encrypt(m, PK, g, p):
    r = random.randint(1, p-2)
    c1 = pow(g, r, p)
    c2 = (m*pow(PK, r)) % p
    return (c1, c2)

def find_bob_sk(PK, g , p):
    for b_sk in range(1, p-2):
        if pow(g, b_sk, p) == PK:
            return b_sk

def decrypt(c, b_sk):
    c1, c2 = c
    c1_sk = pow(c1, b_sk, p)
    c1_sk_inv = pow(c1_sk, -1, p)
    m = (c2*c1_sk_inv) % p
    return m

def modify_encypted_message(c):
    c1, c2 = c
    c2_prime = c2 * 3 % p
    return (c1, c2_prime)


c = encrypt(m, PK, g, p)
sk = find_bob_sk(PK, g, p)
print(f"Bob's private key: {sk}")
original_m = decrypt(c, sk)
print(f"Decrypted message: {original_m}")
c_prime = modify_encypted_message(c)
modified_m = decrypt(c_prime, sk)
print(f"Decrypted modified message: {modified_m}")
