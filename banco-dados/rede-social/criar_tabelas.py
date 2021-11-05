from sqlalchemy import *

from model.models import Usuario, Publicacao

engine = create_engine("mysql+pymysql://herbertc_root:herbertr00t@herbert.cefetvga.pro.br/herbertc_company?charset=utf8mb4", echo=True)

usuario = Usuario.__table__
usuario.create(engine, checkfirst=True)

Publicacao.__table__.create(engine, checkfirst=True)
