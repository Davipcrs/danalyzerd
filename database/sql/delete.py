from database.create_connection import ENGINE
from database.models.note import Note
from sqlalchemy import delete


def delete_note(id_note: int):
    stm = delete(Note).where(Note.id_note == id_note)

    with ENGINE.connect() as conn:
        result = conn.execute(statement=stm)

        conn.commit()
    return result.rowcount
