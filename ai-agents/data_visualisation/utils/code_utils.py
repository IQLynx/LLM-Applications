import re

pattern = re.compile(r"```python\n(.*?)\n```", re.DOTALL)

def match_code_blocks(llm_response: str) -> str:
    """Extract Python code blocks from the LLM response."""
    match = pattern.search(llm_response)
    if match:
        code = match.group(1)
        return code
    return ""