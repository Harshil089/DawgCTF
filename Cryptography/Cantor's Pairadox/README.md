# Counter's Paradox - CTF Writeup

**Challenge Name:** Counter's Paradox  
**Category:** Cryptography / Reverse Engineering  
**Difficulty:** Medium  
**Author:** [Your Name]  

## Challenge Description
We are given:
1. `output.txt` - Contains a single large number representing the encrypted flag
2. `counter's paradox.py` - The encryption script that transforms the flag into the large number

Our goal is to reverse the encryption process to recover the original flag.

## Solution Approach

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
