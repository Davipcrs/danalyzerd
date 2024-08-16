from sqlalchemy import create_engine
from modules.conf.get import *
from models.note import Note


def __init_conn():
    """Create connection"""
    engine = create_engine(
        f"postgresql+pg8000://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
    Note.__table__.create(bind=engine, checkfirst=True)
    return engine


ENGINE = __init_conn()
