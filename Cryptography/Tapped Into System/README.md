# Tapped Into System
> 100pts

## Breifing
The attackers tapped into the system with ease, quickly spreading the news among each other and motivating one another to continue.

... .. ... ... ... .. . .. .. .. . . . .. .. . . ... .. ... ... ... ... . ... ..

*format: SESH{word_word}

## Solution
The provided file can be found [here](tap.png).

Each dot can be broken into pairs, which are in counts of one, two or three.

From here, each pair is a coordinate within the image - E.G. `... .` is `Row 3, Col 1`.

```
... .. = (3, 2) = S
... ... = (3, 3) = E
... .. = (3, 2) = S
. .. = (1, 2) = H
.. .. = (2, 2) = G
. . = (1, 1) = O
. .. = (1, 2) = H
.. . = (2, 1) = A
. ... = (1, 3) = C
.. ... =  (2, 3) = K
... ... = (3, 3) = E
... . = (3, 1) = R
... .. = (3, 2) = S
```

## Flag
Flag: `SESH{GO_HACKERS}`