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
