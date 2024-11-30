-- Generated on: 2024-11-26 17:58:34
-- Dataset: llm_benchmark

-- Original Excel sheet: LLM
CREATE TABLE IF NOT EXISTS llm (
    model_name TEXT  -- Original column: Model Name,
    org TEXT  -- Original column: Org,
    model_size TEXT  -- Original column: Model Size,
    open_src TEXT  -- Original column: Open-Src?,
    description TEXT  -- Original column: Description,
    done TEXT  -- Original column: Done,
    use_case TEXT  -- Original column: Use-case,
    time_took TEXT  -- Original column: Time-took,
    comment TEXT  -- Original column: Comment
);

-- Original Excel sheet: Question-results
CREATE TABLE IF NOT EXISTS question_results (
    question REAL  -- Original column: Question,
    sql_generated REAL  -- Original column: SQL (generated),
    plotly_generated REAL  -- Original column: plotly (generated),
    comment REAL  -- Original column: comment,
    sql_questions TEXT  -- Original column: SQL Questions,
    gpt_4 TEXT  -- Original column: gpt-4,
    gpt_4o TEXT  -- Original column: Gpt -4o,
    gpt_4o_mini TEXT  -- Original column: Gpt -4o-mini,
    gpt_3_5_turbo TEXT  -- Original column: gpt-3.5-turbo,
    claude_3_5_sonnet TEXT  -- Original column: Claude-3.5-sonnet,
    claude_3_sonnet TEXT  -- Original column: Claude-3-sonnet,
    gemini_1_5_pro TEXT  -- Original column: Gemini-1-.5-pro,
    qwen_2_5_coder_7_b TEXT  -- Original column: Qwen 2.5 Coder [7B],
    qwen_2_5_7_b TEXT  -- Original column: Qwen 2.5 [7B],
    qwen_2_5_1_5_b TEXT  -- Original column: Qwen 2.5 [1.5B],
    deepseek_coder_v2_16_b REAL  -- Original column: deepseek-coder-v2 [16B],
    llama_3_1_8_b TEXT  -- Original column: Llama 3.1 [8B],
    llama_3_8_b TEXT  -- Original column: Llama 3 [8B],
    gemma_2_7_b TEXT  -- Original column: Gemma 2 [7B],
    mistral_nemo TEXT  -- Original column: Mistral-nemo,
    mistral TEXT  -- Original column: Mistral,
    codegeex4_9_b TEXT  -- Original column: codegeex4 [9B],
    starcoder2_7_b TEXT  -- Original column: starcoder2 [7B]
);

-- Original Excel sheet: Resources
CREATE TABLE IF NOT EXISTS resources (
    title TEXT  -- Original column: title,
    description REAL  -- Original column: description,
    url TEXT  -- Original column: URL,
    url2 TEXT  -- Original column: URL2
);
