# Private Investigitter Part 2: Unfocused
> 100pts

## Briefing
Can you find Mac's password?

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

If we are fixing the README in 6, we should jump to 7:

```console
alice@AC-LAPTOP:/mnt/c/Users/Alice/Downloads/git_archive/Private Investigitter$ git reset --hard HEAD@{7}
HEAD is now at 1d1a373 Add instructions again, didn't work
```

Opening up the README, we see the following:

```
git add -A
git commit -m "Add instructions"
git push
myG1tHUBSecR3TPhr4se
```

## Flag
Flag: `SESH{myG1tHUBSecR3TPhr4se}`