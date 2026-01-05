# Ubuntu VM Debug and Commit Workings

## Check Antigravity Brain
* If we need the implementation plan / walkthrough / task markdown files, please visit `/home/ubuntu/.gemini/antigravity/brain`

## Git Commit Config
This config is used for commits
```bash
git config --global user.email "ubuntu@ubuntu.com"
git config --global user.name "ubuntu"
```

## After Hibernating Computer, Fix Git Push Issue with the Socket
* Find GitHub sock in Antigravity IDE - when connected to Lambda VM and pushing changes to GitHub (and u reopened a coding session)
```bash
echo $VSCODE_GIT_IPC_HANDLE
```

* To fix git push issue with socket
  * Error: `connect ECONNREFUSED /run/user/1000/vscode-git-3bc78ed735.sock`
  * Fix: Open a new terminal tab and continue `git push` and your work there