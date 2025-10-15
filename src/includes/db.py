import psycopg2
import settings

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

class Db:

	def Connect(write=False,raw=False):
		
		try:
			return psycopg2.connect(
				host=settings.DB_HOST_WRITER if write else settings.DB_HOST_READER,
				port=settings.DB_PORT,
				user=settings.DB_USER,
				password=settings.DB_PASS,
				dbname = None if raw else settings.DB_NAME
			)
		
		except Exception as e:
			print("DB connection error:", e)
		
			return None

	def Disconnect(conn):
		
		try:
			conn.close()
			return True
		
		except Exception as e:
			print("DB disconnect error:", e)
		
			return False
		
	def FetchOne(query,inputs=None,write=False,raw=False):
		
		conn = Db.Connect(write,raw)
		
		if not conn:
			return None
		
		try:
			cur = conn.cursor()
			cur.execute(query,inputs)
			result = cur.fetchone()
			cur.close()
			Db.Disconnect(conn)
		
			return result
		
		except Exception as e:
			print("DB fetch error:",e)
			Db.Disconnect(conn)
		
			return None

	def ExecuteQuery(query,inputs=None,write=False,raw=False,autocommit=False):
		
		conn = Db.Connect(write,raw)
		
		if not conn:
			return False
		
		try:
			conn.autocommit = autocommit
			cur = conn.cursor()
			cur.execute(query,inputs)
			conn.commit()
			cur.close()
			Db.Disconnect(conn)
		
			return True
		
		except Exception as e:
			print("DB error:", e)
			Db.Disconnect(conn)
		
			return False
		
	def GetEngine(write=False):

		host = settings.DB_HOST_WRITER if write else settings.DB_HOST_READER
		url = f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASS}@{host}:{settings.DB_PORT}/{settings.DB_NAME}"
		engine = create_engine(url, echo=settings.FASTAPI_DEBUG)
		
		return engine
	
	def GetSession(write=False):
		
		engine = Db.GetEngine(write)
		Session = sessionmaker(bind=engine)
		
		return Session()
	
	@contextmanager
	def SessionScope(write=False):
		
		session = None
		
		try:
			session = Db.GetSession()
			yield session
			session.commit()
		
		except Exception as e:
			if session:
				session.rollback()
			print(f" Session Error: {e}")
		
		finally:
			if session:
				session.close()