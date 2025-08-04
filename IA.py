import atexit
import os
from pathlib import Path
import subprocess
from typing import Union

import dspy

# Define os caminhos
base_dir = Path.home() / "Desktop" / "LLM"
exe_path = base_dir / "llama" / "llama-server.exe"
model_path = base_dir / "Qwen3-4B-Q4_K_M.gguf"

print(exe_path, model_path)
# Executa o subprocesso
SERVER_PORT = '7777'
with open('log.txt', 'w') as logfile:
  llama_process = subprocess.Popen(
    [str(exe_path), "-m", str(model_path), '--port', SERVER_PORT],
        stdout=logfile,
        stderr=logfile
)

atexit.register(lambda: llama_process.terminate())

lm = dspy.LM(
    model="openai/qwen3",
    api_base=f"http://127.0.0.1:{SERVER_PORT}/v1",
    api_key="local",
    model_type="chat"
)
dspy.configure(lm=lm)

knowledge_base = Path('./')

print([
    arquivo 
    for arquivo in os.listdir(knowledge_base)
    if os.path.splitext(os.path.join(knowledge_base, arquivo))[1] == ".md"
])

"""
    Com 
"""