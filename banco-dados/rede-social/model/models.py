from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Usuario(Base):
    # indica o nome da tabela no BD
    __tablename__ = 'usuario'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)

    nome = Column(String(25))
    data_nascimento = Column(Date)

    #referencia para as publicacoes do usuario. Exemplo de uso: create2()
    publicacoes = relationship("Publicacao",backref='Usuario', lazy=True)

    def __repr__(self):
        return f'Usuario {self.nome}'

    # uma pratica comum eh criar as queries como um metodo estatio @classmethod
    @classmethod
    def find_by_email(cls, session, email):
        return session.query(cls).filter_by(email=email).one()


# Definindo um relacionamento 1:N . Usuario pode ter varias Publicacoes. Usuario eh a classe parent e Publicacao a classe child
# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
class Publicacao(Base):
    # indica o nome da tabela no BD
    __tablename__ = 'publicacao'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    descricao = Column(String(255), nullable=True)

    #cria a chave estrangeira
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    # opcional, criar referencia para o objeto. Exemplo de uso create3()
    usuario = relationship("Usuario", backref="Publicacao")


    def __repr__(self):
        return f'Publicacao {self.descricao}'
