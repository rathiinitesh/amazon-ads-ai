from pydantic import BaseModel


class SQLValidationResult(BaseModel):
    is_valid: bool
    sql: str
    error: str | None = None
