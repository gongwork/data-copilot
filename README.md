# data-copilot

An streamlit app built for data professionals, powered by [vanna.ai](https://github.com/vanna-ai).

## Setup

prepare `.env` file (see `.env.example`) by setting API_KEY for the LLM providor of choice.

```
conda create -n data_copilot python=3.11
conda activate data_copilot
pip install -r requirements.txt 

streamlit run Data-Copilot.py
```

open browser at URL: http://localhost:8501

### Notes
- [plotly 5.23.0 is incompatible with vanna 0.7.4](https://github.com/vanna-ai/vanna/issues/704)

## Demo Video

[Data Copilot for Self-Service Analytics](https://www.youtube.com/watch?v=RKSlUAFmbaM)



## GPU selection
see [Ollama GPU docs](https://github.com/ollama/ollama/blob/main/docs%2Fgpu.md)

```
nvidia-smi      # see GPU memory info
nvidia-smi -L   # see GPU UUID
```

### GPU Suspend/Resume
After Linux suspect, sometimes Ollama will fail to discover your NVIDIA GPU, and fallback to running on the CPU.

To workaround this driver bug by reloading the NVIDIA UVM driver with 
```
sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm
```

To off-load all models in use, restart ollama service
```
sudo systemctl restart ollama
nvidia-smi      # see GPU memory info
```

## AWS Bedrock

### quick start
https://github.com/build-on-aws/amazon-bedrock-quick-start


## Changes

- [2024-08-03] add IMDB movie dataset
evaluate the same questions as asked in https://www.kaggle.com/code/priy998/imdb-sqlite/notebook

- [2024-07-21] upgrade Vanna from `0.6.2` to `0.6.3` to support AWS Bedrock