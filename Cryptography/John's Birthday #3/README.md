# John's Birthday #3
> 150pts

## Briefing
There is a box with combination lock and another note.

" N=581326495398110212146042619557353966378860538548260534904033 e=65537 c=365587980939016547440342497330460850593355300769719679511084 "

What is the plaintext?

## Solution
This challenge is a class RSA with small primes:

```python
# N is in factordb: http://factordb.com/index.php?query=581326495398110212146042619557353966378860538548260534904033

# This gives us the two primes, p and q
p = 564819669946735512444543556507
q = 1029224947942998075080348647219
N = p * q
e = 65537
c = 365587980939016547440342497330460850593355300769719679511084
# I use sage which has inverse_mod but the number is below
# d = inverse_mod(e, (p - 1) * (q - 1))
d = 473429345848655512960171090125418836750969601494870736497605
m = pow(c, d, N)
flag = m.to_bytes(m.bit_length() // 8 + 1, "big")
print(flag.decode())
```

## Flag
Flag: `SESH{RSA_CRACKER{0327}}`