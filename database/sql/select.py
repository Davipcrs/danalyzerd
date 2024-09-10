from database.create_connection import ENGINE
from database.models.note import Note
from sqlalchemy import select


def select_all_notes():
    stm = select(Note)

    with ENGINE.connect() as conn:
        result = conn.execute(statement=stm)

    return result.all()[0]


def select_one_note(id_note: int):
    stm = select(Note).where(Note.id_note == id_note)

    with ENGINE.connect() as conn:
        result = conn.execute(statement=stm)

    return result.all()[0]


def select_notes_by_day(day: str):

    stm = select(Note).where(Note.str_day == day)

    with ENGINE.connect() as conn:
        result = conn.execute(statement=stm)

    return result.all()[0]
