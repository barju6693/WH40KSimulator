from pydantic import BaseModel

from app.models.DataSheet import DataSheet


class Codex(BaseModel):
    name: str
    data_sheets: list[DataSheet]