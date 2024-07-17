# database.py
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine('sqlite:///db_info.db')
metadata = MetaData()

# Tabla de bases de datos
databases = Table('databases', metadata,
    Column('id', Integer, primary_key=True),
    Column('db_name', String, nullable=False),
    Column('classification', String, nullable=False)
)

# Tabla de propietarios
owners = Table('owners', metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False, unique=True)
)

# Tabla de gerentes
managers = Table('managers', metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False, unique=True)
)

# Tabla intermedia
database_owners_managers = Table('database_owners_managers', metadata,
    Column('database_id', Integer, ForeignKey('databases.id'), primary_key=True),
    Column('owner_id', Integer, ForeignKey('owners.id'), primary_key=True),
    Column('manager_id', Integer, ForeignKey('managers.id'), primary_key=True)
)

def create_tables():
    metadata.create_all(engine)

def insert_record(conn, db_record, owner_email, manager_email):
    # Insertar o encontrar el propietario
    owner_result = conn.execute(owners.select().where(owners.c.email == owner_email))
    owner = owner_result.fetchone()
    if owner is None:
        owner_id = conn.execute(owners.insert().values(email=owner_email)).inserted_primary_key[0]
    else:
        owner_id = owner[0]  # Cambiado a índice 0

    # Insertar o encontrar el gerente
    manager_result = conn.execute(managers.select().where(managers.c.email == manager_email))
    manager = manager_result.fetchone()
    if manager is None:
        manager_id = conn.execute(managers.insert().values(email=manager_email)).inserted_primary_key[0]
    else:
        manager_id = manager[0]  # Cambiado a índice 0

    # Insertar la base de datos
    db_id = conn.execute(databases.insert().values(
        db_name=db_record['db_name'],
        classification=db_record['classification']
    )).inserted_primary_key[0]

    # Insertar la relación en la tabla intermedia
    conn.execute(database_owners_managers.insert().values(
        database_id=db_id,
        owner_id=owner_id,
        manager_id=manager_id
    ))

def fetch_all_records(conn):
    result = conn.execute(databases.select())
    return result.fetchall()
