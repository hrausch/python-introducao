from sqlalchemy import *

from model.usuario import Usuario

engine = create_engine("mysql+pymysql://root:root@localhost/rede_social?charset=utf8mb4", echo=True)

usuario = Usuario.__table__
usuario.create(engine, checkfirst=True)