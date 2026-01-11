# Submission Process

## 1. Update the main branch from my repo
```bash
kaiqu@kai-aftershock MINGW64 ~/Downloads/agentbeats-lambda (main)
$ git pull
Already up to date.
```

## 2. Add the upstream AgentBeats Lambda repo to pull the latest changes (if any)
```bash
kaiqu@kai-aftershock MINGW64 ~/Downloads/agentbeats-lambda (main)
$ git remote add upstream https://github.com/LambdaLabsML/agentbeats-lambda.git

kaiqu@kai-aftershock MINGW64 ~/Downloads/agentbeats-lambda (main)
$ git fetch upstream
remote: Enumerating objects: 29, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 29 (delta 8), reused 8 (delta 8), pack-reused 17 (from 1)
Unpacking objects: 100% (29/29), 9.65 KiB | 120.00 KiB/s, done.
From https://github.com/LambdaLabsML/agentbeats-lambda
 * [new branch]      glitchinthematrix    -> upstream/glitchinthematrix
 * [new branch]      lambda/default-llm   -> upstream/lambda/default-llm
 * [new branch]      lambda/update-readme -> upstream/lambda/update-readme
 * [new branch]      main                 -> upstream/main

kaiqu@kai-aftershock MINGW64 ~/Downloads/agentbeats-lambda (main)
$ git checkout main
Already on 'main'
Your branch is up to date with 'origin/main'.

kaiqu@kai-aftershock MINGW64 ~/Downloads/agentbeats-lambda (main)
$ git merge upstream/main
Already up to date.
```

## 3. Re-validate the status of the main branch
```bash
kaiqu@kai-aftershock MINGW64 ~/Downloads/agentbeats-lambda (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## 4. Navigate to the submission directory to prepare cmds
```bash
kaiqu@kai-aftershock MINGW64 ~/Downloads/agentbeats-lambda (main)
$ cd scenarios/security_arena/submissions/heretolearn

kaiqu@kai-aftershock MINGW64 ~/Downloads/agentbeats-lambda/scenarios/security_arena/submissions/heretolearn (main)
$ ls
base64bandit/  crmcrack/  gymjailbreak/  insuranceinsider/
```

## 5. Check out each branch, put in specific files for the scenario AND take out other scenario and test files
* Check I am on the main branch and it is up to date with my repo
```bash
kaiqu@kai-aftershock MINGW64 ~/Downloads/agentbeats-lambda/scenarios/security_arena/submissions/heretolearn (main)
$ # Make sure 
git checkout main
git pull origin main
Already on 'main'
Your branch is up to date with 'origin/main'.
From https://github.com/KaiquanMah/agentbeats-lambda
 * branch            main       -> FETCH_HEAD
Already up to date.
```

* base64bandit
```bash
kaiqu@kai-aftershock MINGW64 ~/Downloads/agentbeats-lambda/scenarios/security_arena/submissions/heretolearn (main)
$ git checkout -b submission/heretolearn/base64bandit
Switched to a new branch 'submission/heretolearn/base64bandit'

# Add ONLY the files for this specific scenario
git add scenarios/security_arena/submissions/heretolearn/base64bandit/
# Remove other scenario files
git rm -r scenarios/security_arena/submissions/heretolearn/crmcrack
git rm -r scenarios/security_arena/submissions/heretolearn/gymjailbreak
git rm -r scenarios/security_arena/submissions/heretolearn/insuranceinsider
git rm -r workings
git rm -r results



# Commit with the exact format
git commit -m "Submission: heretolearn - base64bandit"

# Push to your fork
git push origin submission/heretolearn/base64bandit
```

* crmcrack
```bash
git checkout -b submission/heretolearn/crmcrack
git add scenarios/security_arena/submissions/heretolearn/crmcrack/
# Remove other scenario files
git rm -r scenarios/security_arena/submissions/heretolearn/base64bandit
git rm -r scenarios/security_arena/submissions/heretolearn/gymjailbreak
git rm -r scenarios/security_arena/submissions/heretolearn/insuranceinsider
git rm -r workings
git rm -r results
git commit -m "Submission: heretolearn - crmcrack"
git push origin submission/heretolearn/crmcrack
```

* gymjailbreak
```bash
git checkout -b submission/heretolearn/gymjailbreak
git add scenarios/security_arena/submissions/heretolearn/gymjailbreak/
# Remove other scenario files
git rm -r scenarios/security_arena/submissions/heretolearn/base64bandit
git rm -r scenarios/security_arena/submissions/heretolearn/crmcrack
git rm -r scenarios/security_arena/submissions/heretolearn/insuranceinsider
git rm -r workings
git rm -r results
git commit -m "Submission: heretolearn - gymjailbreak"
git push origin submission/heretolearn/gymjailbreak
```

* insuranceinsider
```bash
git checkout -b submission/heretolearn/insuranceinsider
git add scenarios/security_arena/submissions/heretolearn/insuranceinsider/
# Remove other scenario files
git rm -r scenarios/security_arena/submissions/heretolearn/base64bandit
git rm -r scenarios/security_arena/submissions/heretolearn/crmcrack
git rm -r scenarios/security_arena/submissions/heretolearn/gymjailbreak
git rm -r workings
git rm -r results
git commit -m "Submission: heretolearn - insuranceinsider"
git push origin submission/heretolearn/insuranceinsider
```

## 6. Submit pull requests for each scenario
* Also check again that in each pull request for each scenario's branch, submit only the correct scenario files


## 7. Check the pull requests
* base64bandit - https://github.com/LambdaLabsML/agentbeats-lambda/pull/6/files
* crmcrack - https://github.com/LambdaLabsML/agentbeats-lambda/pull/7/files
* gymjailbreak - https://github.com/LambdaLabsML/agentbeats-lambda/pull/8/files
* insuranceinsider - https://github.com/LambdaLabsML/agentbeats-lambda/pull/9/files
