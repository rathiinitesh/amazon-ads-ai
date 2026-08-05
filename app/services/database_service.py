from sqlalchemy import text

from app.db.session import SessionLocal


class DatabaseService:
    def __init__(self):
        self.db = SessionLocal()

    def execute_query(self, sql: str) -> list[dict]:
        """
        Execute a SELECT query and return the results
        as a list of dictionaries.
        """

        result = self.db.execute(text(sql))

        return [dict(row._mapping) for row in result]
