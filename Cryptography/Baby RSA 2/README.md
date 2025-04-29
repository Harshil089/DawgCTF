# Baby RSA 2

We are given an RSA cryptosystem where extra information (`e_pub` and `d_pub`) has been leaked. Our goal is to recover the original flag from the provided ciphertext.

## Files Provided
- `output-3.txt`: Contains leaked public exponent, private exponent, modulus, and ciphertext
- `chall.py`: Original RSA implementation script

## Solution Approach

### Step 1: Analyzing the Given Information

From the files, we have:
- Public modulus `N`
- Ciphertext `c`
- Leaked public exponent `e_pub = 58271`
- Leaked private exponent `d_pub`
- Standard private exponent `e_priv = 65537`

### Step 2: Mathematical Foundation

The key insight is that both exponents share the same modulus `N` and Euler's totient `φ(N)`. We can use the relationship:

`e_pub × d_pub ≡ 1 mod φ(N)1`


This implies: `(e_pub × d_pub) mod φ(N) == 1`


### Step 4: Computing Private Key

Once φ(N) is found:
1. Compute `d_priv = inverse(e_priv, φ(N))`
2. Decrypt the ciphertext: `m = pow(c, d_priv, N)`


### Step 5: Implementing the Solution

Since we couldn't use external libraries:
- Implemented Extended Euclidean Algorithm for modular inverse
- Created manual `long_to_bytes` conversion

#### Final Exploit Code
The exploit code named Baby RSA 2  (python file) will give the final flag.

### Step-6:
Running the exploit script gives:

[+] Found phi = 119082667712915497270407702277886743652985638444637188059938681008077058895935345765407160513555112013190751711213523389194925328565164667817570328474785369923141707902017088135423556822634292080325835436596781682470966570488860042197957741573421392567389152685718980575218077054212467292718978015646530270836

[+] Found d_priv = 96120864885686403186056234653710251296869558779335447890058382674325593414330527655981183013672664685563739040895912038824046719884907928766185061512064117505137500160469718820878376427321269680474185492103235592149688444372807669442787502162656082317086320354525444747685067613223667848464744144951728814673

[+] Flag: DawgCTF{kn0w1ng_d_1s_kn0w1ng_f4ct0rs}

### Step-7:
Hence the final flag is `DawgCTF{kn0w1ng_d_1s_kn0w1ng_f4ct0rs}`
