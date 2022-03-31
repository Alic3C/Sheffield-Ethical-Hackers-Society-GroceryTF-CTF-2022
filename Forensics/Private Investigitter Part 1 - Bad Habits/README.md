# Private Investigitter Part 1: Bad Habits
> 100pts

## Briefing
You've been hired by the SESH Committee to figure out which members have been violating basic security principles so they can be kicked out of the society. Can you take a look through the attached git repository and find incriminating evidence?

Part 1: Find the email of the committee member who committed vulnerable code (flag format: SESH{email})

Author: Mac

## Solution
The provided file can be found [here](git_archive.zip).

A quick grep search shows an email address which stands out more than the others:

```console
alice@AC-LAPTOP:/mnt/c/Users/Alice/Downloads/git_archive$ grep -E "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b" ./ -r
./Private Investigitter/.git/config:    email = mac@ctf.shefesh.com
./Private Investigitter/.git/config:    url = git@secretgit.shefesh.com:Mac/SESHConfigurations.git
./Private Investigitter/.git/logs/HEAD:0000000000000000000000000000000000000000 04b70dd373eebd0de1a3efeb117e839789d30c42 Mac <mac@ctf.shefesh.com> 1646691651 +0000     commit (initial): Initial commit
./Private Investigitter/.git/logs/HEAD:04b70dd373eebd0de1a3efeb117e839789d30c42 75483e763ed72bff98e2111756235901b1bf601c Nick <nick@ctf.shefesh.com> 1646693038 +0000   commit: Add file viewer
./Private Investigitter/.git/logs/HEAD:75483e763ed72bff98e2111756235901b1bf601c bf844acf1e3a5ccf6fc230b08e814ba06fb8b479 Mac <mac@ctf.shefesh.com> 1646693586 +0000     commit: Fix Nick's terrible code
./Private Investigitter/.git/logs/HEAD:bf844acf1e3a5ccf6fc230b08e814ba06fb8b479 1d1a3735e03c8c8e4b49f868a7f67086a8e92a3b Mac <mac@ctf.shefesh.com> 1646693918 +0000     commit: Add instructions again, didn't work
./Private Investigitter/.git/logs/HEAD:1d1a3735e03c8c8e4b49f868a7f67086a8e92a3b d5f2d1cff6f8b70a2d9f6c44ae52017d96747879 Mac <mac@ctf.shefesh.com> 1646693994 +0000     commit: Fix README
./Private Investigitter/.git/logs/HEAD:d5f2d1cff6f8b70a2d9f6c44ae52017d96747879 18a4c9825ce07df0afa9abbab57106b63c24b9e0 Nicki <nicki@ctf.shefesh.com> 1646826624 +0000 commit: Add AWS Details
./Private Investigitter/.git/logs/HEAD:18a4c9825ce07df0afa9abbab57106b63c24b9e0 07b2777e07a5cdf01ce1e338aa98b33f47815326 Nicki <nicki@ctf.shefesh.com> 1646826711 +0000 commit: Format creds for web display
./Private Investigitter/.git/logs/HEAD:07b2777e07a5cdf01ce1e338aa98b33f47815326 5cb84062cc3f9de1f9c2b904ca7d6ebeaae31ce7 Nick <nick@ctf.shefesh.com> 1646826811 +0000   commit: Add docker configuration details
./Private Investigitter/.git/logs/HEAD:5cb84062cc3f9de1f9c2b904ca7d6ebeaae31ce7 5cb84062cc3f9de1f9c2b904ca7d6ebeaae31ce7 Mac <mac@ctf.shefesh.com> 1646826966 +0000     reset: moving to HEAD
./Private Investigitter/.git/logs/HEAD:5cb84062cc3f9de1f9c2b904ca7d6ebeaae31ce7 29ce732955545250a51a7edf0d7153136a8cfb9f Mac <mac@ctf.shefesh.com> 1646826980 +0000     commit: Clean up repo - again!
./Private Investigitter/.git/logs/HEAD:29ce732955545250a51a7edf0d7153136a8cfb9f ffa71e42187bb000f1928b9d610a0a3612b25945 Mac <mac@ctf.shefesh.com> 1646826996 +0000     commit: Update README.md
./Private Investigitter/.git/logs/refs/heads/master:0000000000000000000000000000000000000000 04b70dd373eebd0de1a3efeb117e839789d30c42 Mac <mac@ctf.shefesh.com> 1646691651 +0000        commit (initial): Initial commit
./Private Investigitter/.git/logs/refs/heads/master:04b70dd373eebd0de1a3efeb117e839789d30c42 75483e763ed72bff98e2111756235901b1bf601c Nick <nick@ctf.shefesh.com> 1646693038 +0000      commit: Add file viewer
./Private Investigitter/.git/logs/refs/heads/master:75483e763ed72bff98e2111756235901b1bf601c bf844acf1e3a5ccf6fc230b08e814ba06fb8b479 Mac <mac@ctf.shefesh.com> 1646693586 +0000        commit: Fix Nick's terrible code
./Private Investigitter/.git/logs/refs/heads/master:bf844acf1e3a5ccf6fc230b08e814ba06fb8b479 1d1a3735e03c8c8e4b49f868a7f67086a8e92a3b Mac <mac@ctf.shefesh.com> 1646693918 +0000        commit: Add instructions again, didn't work
./Private Investigitter/.git/logs/refs/heads/master:1d1a3735e03c8c8e4b49f868a7f67086a8e92a3b d5f2d1cff6f8b70a2d9f6c44ae52017d96747879 Mac <mac@ctf.shefesh.com> 1646693994 +0000        commit: Fix README
./Private Investigitter/.git/logs/refs/heads/master:d5f2d1cff6f8b70a2d9f6c44ae52017d96747879 18a4c9825ce07df0afa9abbab57106b63c24b9e0 Nicki <nicki@ctf.shefesh.com> 1646826624 +0000    commit: Add AWS Details
./Private Investigitter/.git/logs/refs/heads/master:18a4c9825ce07df0afa9abbab57106b63c24b9e0 07b2777e07a5cdf01ce1e338aa98b33f47815326 Nicki <nicki@ctf.shefesh.com> 1646826711 +0000    commit: Format creds for web display
./Private Investigitter/.git/logs/refs/heads/master:07b2777e07a5cdf01ce1e338aa98b33f47815326 5cb84062cc3f9de1f9c2b904ca7d6ebeaae31ce7 Nick <nick@ctf.shefesh.com> 1646826811 +0000      commit: Add docker configuration details
./Private Investigitter/.git/logs/refs/heads/master:5cb84062cc3f9de1f9c2b904ca7d6ebeaae31ce7 29ce732955545250a51a7edf0d7153136a8cfb9f Mac <mac@ctf.shefesh.com> 1646826980 +0000        commit: Clean up repo - again!
./Private Investigitter/.git/logs/refs/heads/master:29ce732955545250a51a7edf0d7153136a8cfb9f ffa71e42187bb000f1928b9d610a0a3612b25945 Mac <mac@ctf.shefesh.com> 1646826996 +0000        commit: Update README.md
```

## Flag
Flag: `SESH{nicki@ctf.shefesh.com}`