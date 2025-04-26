import math

# Given values from output-3.txt
e_pub = 58271
d_pub = 16314065939355844497428646964774413938010062495984944007868244761330321449198604198404787327825341236658059256072790190934480082681534717838850610633320375625893501985237981407305284860652632590435055933317638416556532857376955427517397962124909869006289022084571993305966362498048396739334756594170449299859
N = 119082667712915497270407702277886743652985638444637188059938681008077058895935345765407160513555112013190751711213523389194925328565164667817570328474785391992857634832562389502866385475392702847788337877472422435555825872297998602400341624700149407637506713864175123267515579305109471947679940924817268027249
c = 107089582154092285354514758987465112016144455480126366962910414293721965682740674205100222823439150990299989680593179350933020427732386716386685052221680274283469481350106415150660410528574034324184318354089504379956162660478769613136499331243363223860893663583161020156316072996007464894397755058410931262938
e_priv = 65537  # 0x10001

# Extended Euclidean Algorithm to find modular inverse
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Step 1: Compute k*phi = e_pub * d_pub - 1
ed = e_pub * d_pub - 1

# Step 2: Estimate k (since phi ≈ N)
k = ed // N
# Try nearby k values (k, k+1, k-1) to find correct phi
for candidate_k in [k, k + 1, k - 1]:
    if candidate_k == 0:
        continue
    if ed % candidate_k != 0:
        continue
    phi = ed // candidate_k
    # Verify: e_pub * d_pub ≡ 1 mod phi
    if (e_pub * d_pub) % phi == 1:
        print(f"[+] Found phi = {phi}")
        break
else:
    print("[-] Failed to find phi. Try adjusting k.")
    exit()

# Step 3: Compute d_priv = inverse(e_priv, phi)
try:
    d_priv = modinv(e_priv, phi)
    print(f"[+] Found d_priv = {d_priv}")
except ValueError:
    print("[-] Modular inverse does not exist. Check values.")
    exit()

# Step 4: Decrypt ciphertext (m = c^d_priv mod N)
m = pow(c, d_priv, N)

# Convert m (integer) to bytes (flag)
def long_to_bytes(n):
    return n.to_bytes((n.bit_length() + 7) // 8, 'big')

try:
    flag = long_to_bytes(m).decode('utf-8')
    print(f"[+] Flag: {flag}")
except UnicodeDecodeError:
    print(f"[!] Could not decode as UTF-8. Raw bytes: {long_to_bytes(m)}")