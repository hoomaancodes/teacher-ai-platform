from pathlib import Path

PROMPT_DIR = Path("app/prompts")


def load_prompt(prompt_name: str):

    prompt_path = PROMPT_DIR / f"{prompt_name}.md"

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()