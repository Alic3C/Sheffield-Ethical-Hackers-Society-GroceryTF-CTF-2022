# Robotic
> 50pts

## Breifing
You know where to look, but not what you're looking for.

## Solution
Navigating to `/robots.txt` gives us the [following](https://ctf.shefesh.com/robots.txt):

```
User-agent: *
Allow: /
Disallow: /ctf-management-console
Disallow: /too-easy
```

Going to `/too-easy` shows the [following](https://ctf.shefesh.com/too-easy):

```
Too Easy?
SESH{w4s_th1s_t00_345y}
```

However, this is a fake flag and we need to go to `/w4s_th1s_t00_345y` to find the real [flag](https://ctf.shefesh.com/w4s_th1s_t00_345y):

```
Maybe Not So Easy...
SESH{th15_is_a_l1ttl3_h4rd3r}
```

## Flag
Flag: `SESH{th15_is_a_l1ttl3_h4rd3r}`