# Cipher for good

## Challenge Description
A fellow computer scientist (Bob) crafted this new (old) cipher and sent it over for us to try and crack. Can you help us recover the original message from Bob?

### Step 1: Analyzing the Given Grammar
The provided `challenge.txt` file contains production rules resembling a context-free grammar (CFG).


### Step 2: Initial Approach
Started with the first rule:
1. `A -> JOY`
2. Expanded components:
   - `J -> DawgCTF{`
   - `O -> m0v13_n1gh7`
   - `Y -> }`

This gave: `DawgCTF{m0v13_n1gh7}` (incorrect)

### Step 3: Re-evaluating the Structure
Upon closer inspection, found that `S` was the key non-terminal:
`S -> G U B F`


Broke this down:
1. `G -> cX3P`:
   - `X -> E0CNHCR -> "0mput3r"`
   - `P -> QCD -> "r"`
   - Final: `"c0mput3r"`

2. `U -> _K_`:
   - `K -> Ws -> "1s"`
   - Final: `"_1s_"`

3. `B -> aN_ -> "a_"`

4. `F -> RN0EIZ -> "t00l"`

Combined: `"c0mput3r_1s_a_t00l"`

### Step 4: Final Flag Construction
Wrapped the decoded message in the flag format:
- Prefix: `J -> "DawgCTF{"`
- Suffix: `Y -> "}"`

## Final Flag
`DawgCTF{c0mput3r_1s_a_t00l}`
