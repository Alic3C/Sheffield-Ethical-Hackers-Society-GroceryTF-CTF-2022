# Private Investigitter Part 4: Not Even Remotely Secure
> 100pts

## Briefing
Can you find the domain on which the SESH committee host their git server that they push their code to?

## Solution
Looking within the config file gives us the following information:

```
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[user]
	name = Mac
	email = mac@ctf.shefesh.com
[remote "origin"]
	url = git@secretgit.shefesh.com:Mac/SESHConfigurations.git
	fetch = +refs/heads/*:refs/remotes/origin/*
```

## Flag
Flag: `SESH{secretgit.shefesh.com}`