# Requirements Secretly Analysed
> 250pts

## Breifing
It seems that the owners of the grocery store hid an important message in a list of products that need to be restocked.

However, they fear that its original meaning has been tampered with and all that is left is an altered note left by the attackers. Could you help them confirm that?

"761 Quesadillas 911 Peaches 181 Eggs 3821 Doughnuts Encrypted Message: 677889 "

The decrypted message is a number initially, how would you turn it into letters? The encrypted message can be seen as 67 78 89 (not in computations) and the decrypted message will have the same length in numbers.

*format: SESH{decrypted_word}

## Solution
Python script time!

```python
q = 761
p = 911
N = p * q
e = 181
d = 3821
c = 677889
m = pow(c, d, N)
ms = str(m)
print(bytes([int(ms[i:i+2]) for i in range(0, len(ms), 2)]).decode())
```

## Flag
Flag: `SESH{BYE}`