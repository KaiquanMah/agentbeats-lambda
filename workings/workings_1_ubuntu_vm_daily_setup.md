# Ubuntu VM Daily Setup Workings

When starting a new VM with yesterday's persistent storage, follow these 5 steps to ensure everything is ready for `uv run agentbeats-run`.

## 1. Verify Connection from Antigravity IDE to Lambda VM
* debug ssh connection (for every VM in your Terminal, before u SSH into the VM in antigravity)
```bash
ssh -i /c/Users/<username>/.ssh/your-berkeley-lambda.pem ubuntu@<lambda_vm_ip_address>
```

## 2. SSH into Lambda VM
* Note that from experience, step 1 above is required for Lambda VMs
* Update your `~/.ssh/config` file with the following:
```bash
Host <your-ssh-name>
    HostName <lambda_vm_ip_address>
    User ubuntu
    IdentityFile "C:/Users/<username>/.ssh/your-berkeley-lambda.pem"
```
* Click the bottom left 'SSH' button in antigravity
* Click 'Connect to SSH Host' in the pop-up window > Select <your-ssh-name>

## 3. Verify Hardware (GPU)
Ensure the GPU is correctly detected by the VM.
```bash
nvidia-smi
```

## 4. Start the Inference Server (vLLM)
Start the Docker container for the `gpt-oss-20b` model.
```bash
sudo docker run --gpus all -v /home/ubuntu/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model openai/gpt-oss-20b
```

## 5. Prep the Python Environment
Ensure dependencies are synchronized.
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh && \
source ~/.profile

uv sync
```

## 6. Verify Model Availability
Check if the vLLM server is up and serving the correct model.
```bash
curl http://localhost:8000/v1/models
```

## 7. Run a Submission Scenario
* Run **with internal agent dialogue showing** on the Terminal
```bash
env PYTHONPATH=. uv run agentbeats-run scenarios/security_arena/submissions/heretolearn/insuranceinsider/scenario_insuranceinsider.toml --show-logs
```