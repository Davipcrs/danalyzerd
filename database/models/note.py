from __future__ import annotations
from database.models.base import BASE
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Note(BASE):
    """Note model, used to create the Database Table"""
    __tablename__ = "notes"
    # alter the table to store the time and the date in diferent tables
    # Store in the database in separate to make queries easy
    # Sends and recieves from api in a One format (datetime)
    id_note: Mapped[int] = mapped_column(primary_key=True)
    str_text: Mapped[str] = mapped_column(String)
    str_md_text: Mapped[str] = mapped_column(String)
    # str_date: Mapped[str] = mapped_column(String)
    str_day: Mapped[str] = mapped_column(String)
    str_time: Mapped[str] = mapped_column(String)
    bool_completed: Mapped[bool] = mapped_column(Boolean)
