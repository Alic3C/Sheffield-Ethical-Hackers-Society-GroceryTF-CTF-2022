# Private Investigitter Part 3: Cloudy with a Chance of Secrets
> 100pts

## Briefing
Can you find an AWS Secret Key somewhere in the git repository?

## Solution
Lets take a look at the git history:

```console
alice@AC-LAPTOP:/mnt/c/Users/Alice/Downloads/git_archive/Private Investigitter$ git reflog
ffa71e4 (HEAD -> master) HEAD@{0}: commit: Update README.md
29ce732 HEAD@{1}: commit: Clean up repo - again!
5cb8406 HEAD@{2}: reset: moving to HEAD
5cb8406 HEAD@{3}: commit: Add docker configuration details
07b2777 HEAD@{4}: commit: Format creds for web display
18a4c98 HEAD@{5}: commit: Add AWS Details
d5f2d1c HEAD@{6}: commit: Fix README
1d1a373 HEAD@{7}: commit: Add instructions again, didn't work
bf844ac HEAD@{8}: commit: Fix Nick's terrible code
75483e7 HEAD@{9}: commit: Add file viewer
04b70dd HEAD@{10}: commit (initial): Initial commit
```

4 looks intresting:

```console
alice@AC-LAPTOP:/mnt/c/Users/Alice/Downloads/git_archive/Private Investigitter$ git reset --hard HEAD@{4}
HEAD is now at 07b2777 Format creds for web display
```

In `config`, we can now see [aws.html](aws.html)!

```
Secret Key: AKIAJSIE27KKMHXI3BJQ

5bEYu26084qjSFyclM/f2pz4gviSfoOg+mFwBH39
```

## Flag
Flag: `SESH{AKIAJSIE27KKMHXI3BJQ}`