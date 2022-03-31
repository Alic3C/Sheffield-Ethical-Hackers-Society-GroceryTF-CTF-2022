# Heist Part 1: Where's our Console?
> 50pts

## Breifing
This year the SESH Committee have upgraded their infrastructure from a Raspberry Pi to something more stable and secure! They're so convinced you won't be able to hack it, that they're offering a Raspberry Pi to anyone who can.

Can you find the IP address of our CTF Management Console?

Flag format: SESH{IP}

Author: Mac

## Solution
Visit https://ctf.shefesh.com/robots.txt and you'll see 
```
User-agent: *
Allow: /
Disallow: /ctf-management-console
Disallow: /too-easy
```
Append `/ctf-management-console` to the end of the shefesh url, and you'll be greeted with the below, which contains the IP to the management console.
```
Committee - login to our CTF management console here: http://35.178.187.4
```
## Flag
Flag: `SESH{35.178.187.4}`
