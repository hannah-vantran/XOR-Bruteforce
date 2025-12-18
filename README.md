# XOR Bruteforce
This script uses a hexadecimal ciphertext and a piece of known plaintext to bruteforce all possible XOR key values to decode the ciphertext. This script is optimized for CTF style challenges where the general format of flags is known:
```bash
ctf{flag}
```
## Setup

Tested with Python 3.11.4

## Running

1. Configure ct and k_pt in SOLUTION.py to be the ciphertext and the known plaintext
2. Compile and run SOLUTION.py

## Demo

Configuration:
```bash
ct = "10580f080f44140f2b130d40520f005019003c2100172117081c"
k_pt = "s9{"
```

Output:

```bash
plaintext: s9{kn0wn_pl41nt3xt_@tt@ck} key: 636174
```

## Credit

https://hannahvantran.com/projects/xor-bruteforce
