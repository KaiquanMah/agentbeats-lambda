# Start-of-Day Setup Guide

When starting a new VM with yesterday's persistent storage, follow these 5 steps to ensure everything is ready for `uv run agentbeats-run`.

## 1. Verify Hardware (GPU)
Ensure the GPU is correctly detected by the VM.
```bash
nvidia-smi
```

## 2. Start the Inference Server (vLLM)
Start the Docker container for the `gpt-oss-20b` model.
```bash
sudo docker run --gpus all -v /home/ubuntu/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model openai/gpt-oss-20b
```

## 3. Verify Model Availability
Check if the vLLM server is up and serving the correct model.
```bash
curl http://localhost:8000/v1/models
```

## 4. Prep the Python Environment
Ensure dependencies are synchronized.
```bash
uv sync
```

---

### Verification Complete?
Once these steps are done, you are ready to run an example scenario:
```bash
uv run agentbeats-run scenarios/security_arena/submissions/heretolearn/insuranceinsider/scenario_insuranceinsider.toml
```
