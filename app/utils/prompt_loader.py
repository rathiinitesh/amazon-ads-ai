from pathlib import Path


class PromptLoader:
    _PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

    @classmethod
    def load(cls, prompt_name: str) -> str:
        prompt_path = cls._PROMPTS_DIR / prompt_name

        if not prompt_path.exists():
            raise FileNotFoundError(f"Prompt not found: {prompt_path}")

        return prompt_path.read_text(encoding="utf-8")
