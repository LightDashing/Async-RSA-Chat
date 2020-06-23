import sqlalchemy
from sqlalchemy.types import Integer, Text, VARCHAR, DateTime
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, relationship
from ServerSettings import ServerSettings
import hashlib
import datetime

# engine = sqlalchemy.create_engine('postgresql://postgres:1@localhost:5432/postgres', echo=True,
                                  #pool_pre_ping=True)

Base = declarative_base()


def password_hashing(string):
    return hashlib.md5(bytes(string, 'utf-8')).hexdigest()


class UserData(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(VARCHAR(30), nullable=False, unique=True)
    email = Column(VARCHAR(30), nullable=False, unique=True)
    password = Column(VARCHAR(512), nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __str__(self):
        return f'User_id = {self.id}, User_name={self.login}, Created_at={self.created_at}'


class ServerDB:

    def __init__(self):
        self.ServerSettings = ServerSettings()
        serverdata = self.ServerSettings.get_settings()
        self.engine = sqlalchemy.create_engine(serverdata['server'], echo=True)
        self.session = Session(bind=self.engine)

    def is_user_exist(self, login: str) -> bool:
        self.session = Session(bind=self.engine)
        user = self.session.query(UserData).filter(UserData.login == login).first()
        print(user)
        self.session.close()
        if user:
            return True
        else:
            return False

    def login(self, login: str, password: str) -> bool:
        self.session = Session(bind=self.engine)
        verification = self.session.query(UserData).filter(UserData.login == login,
                                                           UserData.password == password_hashing(password)).first()
        self.session.close()
        print(verification)
        if verification:
            return True
        else:
            return False

    def sign_in(self, login: str, password: str, email: str):
        self.session = Session(bind=self.engine)
        self.session.add(
            UserData(login=login, password=password_hashing(password), email=email, created_at=datetime.datetime.now()))
        self.session.commit()
        self.session.close()


#Base.metadata.create_all(engine)

# session.add(User(id=0, username='Nickolay Chugunnicov', password=password_hashing('!1!2qe@3ry?'),email='chugunnic@gmail.com', updated_at=datetime.datetime.now(), created_at=datetime.datetime.now()))
# session.add(Post(id=0, content='This is ORM-based Postgres Table!', comments='This is so cool! \n I want it too!', created_at=datetime.datetime.now(), created_by=0))
# post = session.query(Post).filter(User.id==0).all()
# print(post[0])
