# Counter's Paradox


## Challenge Description
We are given:
1. `output.txt` - Contains a single large number representing the encrypted flag
2. `counter's paradox.py` - The encryption script that transforms the flag into the large number

Our goal is to reverse the encryption process to recover the original flag.

### Step 1: Analyzing the Encryption Script
The encryption process works as follows:
1. Converts the flag string into ASCII values
2. Pads the array with zeros until its length is a power of two
3. Applies a custom pairing function recursively 6 times
4. Outputs a single large number

Key functions:
- `getTriNumber(n)`: Calculates triangular numbers
- `pair(n1, n2)`: Combines two numbers using triangular numbers
- `pair_array(arr)`: Processes array in pairs
- `pad_to_power_of_two(arr)`: Ensures array length is power of two

### Step 2: Understanding the Mathematics
The pairing function is based on triangular numbers:
`pair(n1, n2) = T(n1 + n2) + n2`
where T(k) = k*(k+1)//2 (triangular number)


To reverse this, we need to:
1. Given p = pair(n1, n2), find S where T(S) ≤ p < T(S+1)
2. Calculate n2 = p - T(S)
3. Calculate n1 = S - n2

### Step 3: Implementing the Decryption
We wrote a Python script (counter's paradox) to reverse the process.

### Step-4:
After reversing the process, here is the final flag: `Dawg{1_pr3f3r_4ppl3s_t0_pa1rs_4nyw2y5}`
