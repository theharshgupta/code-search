from website import db
from website.models import Post
from datetime import timedelta, date, datetime
from sqlalchemy import desc


def create_table():
    from sqlalchemy import create_engine
    from sqlalchemy import MetaData
    from sqlalchemy import Table
    from sqlalchemy import Column
    from sqlalchemy import Integer, String


    db_uri = 'sqlite:///website/site.db'
    engine = create_engine(db_uri)

    meta = MetaData(engine)

    t2 = Table('functions', meta,
    Column('id', Integer, primary_key=True),
    Column('function_name', String(1000)),
    Column('filepath', db.String(1000)),
    Column('function_docstring', db.String(1000)))

    t2.create()

create_table()