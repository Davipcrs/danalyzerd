from sqlalchemy import create_engine


def __init_conn():
    """Create connection"""
    engine = create_engine(
        "postgresql+pg8000://postgres:postgres@host/danalize")
    return engine


ENGINE = __init_conn()
