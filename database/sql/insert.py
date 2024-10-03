from database.create_connection import ENGINE
from database.models.note import Note
from sqlalchemy import insert
from datetime import date, time


def insert_into_note(str_text: str, str_md_text: str, dt_day: date, t_time: time, bool_complete: bool):
    stm = insert(Note).values(str_text=str_text, str_md_text=str_md_text,
                              dt_day=dt_day, t_time=t_time, bool_completed=bool_complete).returning(Note.id_note)

    with ENGINE.connect() as conn:
        result = conn.execute(statement=stm)
        conn.commit()

    return result.all()
