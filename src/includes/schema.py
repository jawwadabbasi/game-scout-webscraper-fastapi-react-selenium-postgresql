import settings

from includes.db import Db
from includes.models import Base

class Schema:

    def CreateDatabase():
        
        check_query = "SELECT 1 FROM pg_database WHERE datname = %s"
        create_query = f"CREATE DATABASE {settings.DB_NAME}"

        exists = Db.FetchOne(check_query, (settings.DB_NAME,), raw=True, write=True)

        if exists:
            print(f"Database '{settings.DB_NAME}' already exists.")
            return True

        if Db.ExecuteQuery(create_query, raw=True, write=True, autocommit=True):
            print(f"Database '{settings.DB_NAME}' created.")
            return True
        
        else:
            print("Failed to create database.")
            return False
        
    def CreateTables():
        
        engine = Db.GetEngine(write=True)
        Base.metadata.create_all(engine)
        print("All tables created successfully.")

        return True