from math import isqrt

def getTriNumber(n):
    return n * (n + 1) // 2

def unpair(p):
    S = (isqrt(8 * p + 1) - 1) // 2
    T_S = getTriNumber(S)
    n2 = p - T_S
    n1 = S - n2
    return (n1, n2)

def reverse_pair_array(encoded, steps=6):
    current = [encoded]
    for _ in range(steps):
        new_current = []
        for num in current:
            n1, n2 = unpair(num)
            new_current.extend([n1, n2])
        current = new_current
    return current

encoded = 4036872197130975885183239290191447112180924008343518098638033545535893348884348262766810360707383741794721392226291497314826201270847784737584016
unpaired = reverse_pair_array(encoded, 6)

# Find the last index where the value is non-zero
last_non_zero = len(unpaired) - 1
while last_non_zero >= 0 and unpaired[last_non_zero] == 0:
    last_non_zero -= 1

# Slice the array up to the last non-zero element
original_ascii = unpaired[:last_non_zero + 1]

# Convert ASCII values to characters
flag = ''.join(chr(c) for c in original_ascii)
print(flag)