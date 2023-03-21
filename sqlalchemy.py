from sqlalchemy import create_engine, Table, Column, Integer, String, Date, MetaData

engine = create_engine('sqlite:///attend_list.db', echo=True)
metadata = MetaData()

attend = Table('attend', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('date', Date),
    Column('status', String)
)

metadata.create_all(engine)

conn = engine.connect()

conn.execute(attend.insert(), [
    {'name': 'Alice', 'date': '2022-03-20', 'status': 'present'},
    {'name': 'Bob', 'date': '2022-03-21', 'status': 'absent'}
])

conn.close()
