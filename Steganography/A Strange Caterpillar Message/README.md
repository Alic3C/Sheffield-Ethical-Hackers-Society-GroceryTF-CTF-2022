# A Strange Caterpillar Message
> 65pts

## Breifing
Our grocery shop is being sued by S&M for a Chris the Caterpillar lookalike, One of informants has sent us a file with a password inside apparently but they just sent us a picture of Chris. I wonder what it could mean...

## Solution
The provided file can be found [here](Our_Lovely_Cake.jpg).

Running `binwalk` on the file provides us with the following:

```console
alice@AC-LAPTOP:/mnt/c/Users/Alice/Downloads$ binwalk -e Our_Lovely_Cake.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
30            0x1E            TIFF image data, little-endian offset of first image directory: 8
478757        0x74E25         Zip archive data, at least v2.0 to extract, compressed size: 24664, uncompressed size: 25801, name: Caterpillar Ception.jpg
503543        0x7AEF7         End of Zip archive, footer length: 22
```

This provides us with a [zip](74E25.zip) and [jpeg](Caterpillar%20Ception.jpg):

![Caterpillar%20Ception.jpg](Caterpillar%20Ception.jpg)

## Flag
Flag: ` `
