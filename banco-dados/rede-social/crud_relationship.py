from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

from model.models import Usuario, Publicacao

engine = create_engine(
    "mysql+pymysql://herbertc_root:herbertr00t@herbert.cefetvga.pro.br/herbertc_company?charset=utf8mb4", echo=True)

Session = sessionmaker(bind=engine)
session = Session()


def create1():
    user1 = Usuario(email='cersei@got.com', senha='123', nome='Cersei Bar.', data_nascimento='1980-01-01')

    publicacao1 = Publicacao(descricao='Meu primeiro tweet')
    user1.publicacoes.append(publicacao1)

    publicacao2 = Publicacao(descricao='Meu segundo tweet')
    user1.publicacoes.append(publicacao2)

    session.add(user1)
    session.commit()

def create2():

    user1 = Usuario(email='arya@got.com', senha='123', nome='Arya Stark', data_nascimento='1980-01-01')
    session.add(user1)
    session.commit()

    publicacao1 = Publicacao(usuario_id=user1.id, descricao='Meu primeiro tweet')
    session.add(publicacao1)
    session.commit()

    publicacao2 = Publicacao(usuario_id=user1.id, descricao='Meu segundo tweet')
    session.add(publicacao2)
    session.commit()

def create3():

    user1 = Usuario(email='john@got.com', senha='123', nome='John Stark', data_nascimento='1980-01-01')

    publicacao1 = Publicacao(usuario=user1, descricao='Meu primeiro tweet')
    session.add(publicacao1)

    publicacao2 = Publicacao(usuario=user1, descricao='Meu segundo tweet')
    session.add(publicacao2)
    session.commit()

# create1()
# create2()
# create3()

# read()
# update()
# delete()
