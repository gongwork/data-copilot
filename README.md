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

## Demo Video

[Data Copilot for Self-Service Analytics](https://www.youtube.com/watch?v=RKSlUAFmbaM)


## AWS Bedrock

### quick start
https://github.com/build-on-aws/amazon-bedrock-quick-start


## Changes

### Vanna upgrade
- [2024-07-21] from `0.6.2` to `0.6.3` to support AWS Bedrock