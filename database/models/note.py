from __future__ import annotations
from database.models.base import BASE
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Note(BASE):
    __tablename__ = "notes"

    id_note: Mapped[int] = mapped_column(primary_key=True)
    str_text: Mapped[str] = mapped_column(String)
    str_md_text: Mapped[str] = mapped_column(String)
    str_date: Mapped[str] = mapped_column(String)
    bool_completed: Mapped[bool] = mapped_column(Boolean)
    
