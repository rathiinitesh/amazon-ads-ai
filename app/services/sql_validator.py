from sqlglot import parse_one
from sqlglot.errors import ParseError
from sqlglot.expressions import Select

from app.models import SQLValidationResult


class SQLValidatorService:
    FORBIDDEN_KEYWORDS = {  # noqa: RUF012
        "ALTER",
        "CALL",
        "CREATE",
        "DELETE",
        "DROP",
        "EXEC",
        "EXECUTE",
        "INSERT",
        "MERGE",
        "REPLACE",
        "TRUNCATE",
        "UPDATE",
    }

    @classmethod
    def validate(cls, sql: str) -> SQLValidationResult:
        sql = sql.strip()

        if not sql:
            return SQLValidationResult(
                is_valid=False,
                sql=sql,
                error="SQL query is empty.",
            )

        # Prevent multiple statements
        if ";" in sql[:-1]:
            return SQLValidationResult(
                is_valid=False,
                sql=sql,
                error="Multiple SQL statements are not allowed.",
            )

        upper_sql = sql.upper()

        for keyword in cls.FORBIDDEN_KEYWORDS:
            if keyword in upper_sql:
                return SQLValidationResult(
                    is_valid=False,
                    sql=sql,
                    error=f"Forbidden keyword detected: {keyword}",
                )

        try:
            parsed = parse_one(sql, dialect="mysql")
        except ParseError as exc:
            return SQLValidationResult(
                is_valid=False,
                sql=sql,
                error=str(exc),
            )

        if not isinstance(parsed, Select):
            return SQLValidationResult(
                is_valid=False,
                sql=sql,
                error="Only SELECT statements are allowed.",
            )

        return SQLValidationResult(
            is_valid=True,
            sql=sql,
        )
