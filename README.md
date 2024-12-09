# data-copilot

An streamlit app built for data professionals, powered by [vanna.ai](https://github.com/vanna-ai).

By streamlining the data-to-insight life-cycle, Data Copilot is a game-changer tool for Self-Service Analytics. Built on cutting-edge GenAI models, it empowers data professionals to unlock insights from data faster than ever, therefore allows them to focus on deeper analysis and strategic decision-making.

## Overview
![welcome](https://raw.githubusercontent.com/gongwork/data-copilot/refs/heads/main/docs/00-data-copilot-arch-design.png)

## Features

- **<span style="color: red;">ChatGPT</span>**: ask general question on <span style="color: blue;">LLM</span> models of choice 
- **<span style="color: red;">RAG</span>**: ask dataset-specific question via Retrieval Augmented Generation
    - **<span style="color: blue;">Semantic Search</span>**: discover data schema
    - **<span style="color: blue;">Text-to-SQL</span>**: generate SQL from plain text
    - **<span style="color: blue;">Data-to-Plot</span>**: generate Python code to visualize data 
- **<span style="color: red;">Data Privacy</span>** (__optional__) : leverage  <span style="color: blue;">Ollama</span> and open-source LLM models locally 


### Configure
Choose data source, vector store, LLM model
![configure](https://raw.githubusercontent.com/gongwork/data-copilot/refs/heads/main/docs/p1-config.png)


### Database
Review database schema, data
![database](https://raw.githubusercontent.com/gongwork/data-copilot/refs/heads/main/docs/p2-database.png)


### Knowledge Base
Define knowledge base with table schema and documentation
![knowledgebase](https://raw.githubusercontent.com/gongwork/data-copilot/refs/heads/main/docs/p3-knowledgebase.png)

### Ask AI
Ask question on data (built on RAG), get answer in SQL, dataframe, python, plotly chart
![rag1](https://raw.githubusercontent.com/gongwork/data-copilot/refs/heads/main/docs/p4-rag-1.png)

![rag2](https://raw.githubusercontent.com/gongwork/data-copilot/refs/heads/main/docs/p4-rag-2.png)

### Results
Question & answer pairs are saved to database
![results](https://raw.githubusercontent.com/gongwork/data-copilot/refs/heads/main/docs/p5-results.png)

### Import Tools
Import data from CSV or connect to database
![import](https://raw.githubusercontent.com/gongwork/data-copilot/refs/heads/main/docs/p9-import-sqlite.png)

### Demo Video

[![Data-Copilot Demo](https://img.youtube.com/vi/RKSlUAFmbaM/0.jpg)](https://www.youtube.com/watch?v=RKSlUAFmbaM)


## Setup

```
conda create -n data_copilot python=3.11
conda activate data_copilot
pip install -r requirements.txt 
cd src
cp .env.example .env   # add API_KEY in .env
streamlit run Data-Copilot.py
```

open browser at URL: http://localhost:8501

## Additional Notes

- Add documentation into knowledgebase to enhance context search
    - prepare a csv file with the following columns
        - business_term
        - business_description
        - related_tables
        - related_columns
    - import it into table `bus_term`
    - see [bus_term.csv](https://github.com/wgong/py4kids/blob/master/lesson-18-ai/vanna/note_book/data/company_rank/bus_term.csv) for example

- [Extra-1](https://raw.githubusercontent.com/gongwork/data-copilot/refs/heads/main/docs/README-extra-1.md)



