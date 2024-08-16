from sqlalchemy import create_engine
from modules.conf.get import *


def __init_conn():
    """Create connection"""
    engine = create_engine(
        f"postgresql+pg8000://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
    return engine


ENGINE = __init_conn()
