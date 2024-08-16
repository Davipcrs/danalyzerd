from database.create_connection import ENGINE
from database.models.note import Note
from sqlalchemy import update


def update_note(id_note: int, str_text: str, str_md_text: str, str_date: str, bool_complete: bool):
    stm = update(Note).where(Note.id_note == id_note).values(str_text=str_text, str_md_text=str_md_text,
                                                             str_date=str_date, bool_complete=bool_complete)

    with ENGINE.connect() as conn:
        result = conn.execute(statement=stm)
        conn.commit()

    return result.rowcount
