from database.create_connection import ENGINE
from database.models.note import Note
from sqlalchemy import update


def update_note(id_note: int, str_text: str, str_md_text: str, str_day: str, str_time: str, bool_complete: bool):
    stm = update(Note).where(Note.id_note == id_note).values(str_text=str_text, str_md_text=str_md_text,
                                                             str_day=str_day, str_time=str_time, bool_complete=bool_complete)

    with ENGINE.connect() as conn:
        result = conn.execute(statement=stm)
        conn.commit()

    return result.rowcount
