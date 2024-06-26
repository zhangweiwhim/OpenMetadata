"""
Oracle models
"""
from typing import List, Optional

from pydantic import BaseModel, Field


class OracleStoredProcedure(BaseModel):
    """Oracle Stored Procedure list query results"""

    name: str
    definition: str
    language: Optional[str] = Field(
        None, description="Will only be informed for non-SQL routines."
    )
    owner: str


class FetchProcedure(BaseModel):
    """Oracle Fetch Stored Procedure Raw Model"""

    owner: Optional[str]
    name: str
    line: int
    text: str


class FetchProcedureList(BaseModel):
    __name__: List[FetchProcedure]
