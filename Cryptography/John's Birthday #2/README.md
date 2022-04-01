# John's Birthday #2
> 100pts

## Briefing
John finally arrived at his destination, and on top of the table was a note, a slip of paper, and a number of sticks of various thicknesses.

Note: "You are very close."

Answer hint: SESH{WORDS_WORDS_WORDS_WORDS} (Join two words with an underscore )

## Solution
The provided file can be found [here](john_birthday2.png).

Writing out the characters from the image, we get:

`R   E   FTOTRO HIPFEG   E   R   A   T   O   R   `

The words are found by indexing them, which allows for us to figure out the flag:

```python
a = "R   E   FTOTRO HIPFEG   E   R   A   T   O   R   "
print(a[::-1])
print(a[::2])
print(a[::4])
print(a[1::4])
print(a[2::4])
print(a[3::4])
```

The output from the script is as follows:

```python
   R   O   T   A   R   E   GEFPIH ORTOTF   E   R
R E FOR IFG E R A T O R 
REFRIGERATOR
  TOP       
  O F       
  THE   
```

## Flag
Flag: `SESH{TOP_OF_THE_REFRIGERATOR}`