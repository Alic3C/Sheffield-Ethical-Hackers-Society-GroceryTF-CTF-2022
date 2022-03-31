# Tyger Tyger, Burning Bright
> 250pts

## Breifing
Among the 192 files of the system, 4 of them are rumoured to contain secret strings, crackable only by a very small percentage of hackers.

Even the attackers spent a significant amount of time investigating them, ROCKING back and forth on their chairs wondering what to pick from the list. Eventually, they found four specific words to be the passwords, their positions in the large file being 35 20 38 (why are these not 2 separate base 10 numbers? how can you make them be?), 6512bd43d9caa6e02c990b0a82652dca and FA35E192121EABF3DABF9F5EA6ABDBCBC107AC3B (identify both and crack)

However, all these files had the same content, a long hash obtained by combining these four words into one word (no spaces, all lowercase) and hashing into the hash that needs to be inferred from the title and first paragraph.

Fortunately for the owners, they never cracked this hash, but they still identified it as being...

*format: SESH{hash}

## Solution
The provided file can be found [here](rock.png).

## Flag
Flag: ` `