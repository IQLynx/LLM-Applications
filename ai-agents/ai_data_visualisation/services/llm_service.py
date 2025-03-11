from together import Together
from utils.code_utils import match_code_blocks


def chat_with_llm(code_interpreter, user_message: str, dataset_path: str, together_api_key: str,
                  model_name: str, st) -> tuple:
    """Interact with Together AI LLM to generate Python code and execute it."""
    system_prompt = f"""You're a Python data scientist and data visualization expert. You are given a dataset at path '{dataset_path}' and also the user's query.
You need to analyze the dataset and answer the user's query with a response and you run Python code to solve them.
IMPORTANT: Always use the dataset path variable '{dataset_path}' in your code when reading the CSV file."""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message},
    ]

    client = Together(api_key=together_api_key)
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
    )

    response_message = response.choices[0].message
    python_code = match_code_blocks(response_message.content)

    if python_code:
        from services.code_interpreter_service import code_interpret
        code_interpreter_results = code_interpret(code_interpreter, python_code, st)
        return code_interpreter_results, response_message.content
    else:
        return None, response_message.content