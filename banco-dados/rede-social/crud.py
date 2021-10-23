from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker


from model.usuario import Usuario

engine = create_engine("mysql+pymysql://root:root@localhost/rede_social?charset=utf8mb4", echo=False)

Session = sessionmaker(bind=engine)
session = Session()

def create():
    # instancia um objeto Usuario para cada tupla que deseja inserir no banco de dados 
    user1 = Usuario(email='cersei@got.com', senha='123', nome='Cersei Bar.', data_nascimento='1980-01-01')
    #adiciona o objeto na session
    session.add(user1) 
    #a operacao no banco ainda não foi executada
    print(user1.id)

    user2 = Usuario(email='arya@got.com', senha='321')
    session.add(user2)
    print(user2.id)  

    #executa a operacao nao banco e atualiza o objeto
    session.commit()

    #perceba que cada objeto agora possui o campo id preenchido com o valor do banco de dados
    print(user1.id)
    print(user2.id)


def read():

    #recupera todas tuplas da tabela Usuario ordenado pelo ID
    # SELECT * FROM Usuario ORDER BY id
    for tupla in session.query(Usuario).order_by(Usuario.id):
        print(tupla.id, " - ", tupla.email)

    #recupera todas tuplas da tabela Usuario - seleciona apenas as colunas email e nome
    # SELECT email, nome FROM Usuario
    for email, nome in session.query(Usuario.email, Usuario.nome):
        print(email, '-' ,  nome)

    # SELECT * FROM Usuario WHERE email='hrf@hrf.com'
    for tuplas in session.query(Usuario).filter(Usuario.email=='hrf@hrf.com'):
        print(tuplas.id, '-', tuplas.nome)

    # SELECT * FROM Usuario WHERE email='hrf@hrf.com' AND nome like '%herbert%'
    for tuplas in session.query(Usuario).\
            filter(Usuario.email=='hrf@hrf.com').\
            filter(Usuario.nome.like('%herbert%')):
        print(tuplas.id, '-', tuplas.nome)

    # SELECT * FROM Usuario WHERE email='hrf@hrf.com' OR nome like '%Cersei%'
    for tuplas in session.query(Usuario).\
            filter(or_(Usuario.email=='hrf@hrf.com',Usuario.nome.like('%Cersei%'))):
        print(tuplas.id, '-', tuplas.nome)

def update():

    #recupera registro do BD
    user = session.query(Usuario).filter(Usuario.id == 3).one()

    #atualiza os valores dos campos que desejar
    user.nome = "Arya Stark"
    user.data_nascimento = '1980-10-30'

    #executa no banco de dados
    session.commit()

    #ou, usando metodos de classe
    user = Usuario.find_by_email(session=session, email='cersei@got.com')
    user.nome = "Cersei Lannister"
    session.commit()


def delete():

    #para remover uma tupla no BD eh preciso que:

    #1 - instancie um objeto da tupla que deseja remover
            #abaixo eh um exemplo de como recuperar um objeto pela chave primaria. Não há a necessidade
            #do filter nessa operação
    user = session.query(Usuario).get(5)

    #2 - adicione a remocao do objeto na session
    session.delete(user)

    #3 - execute a operacao no BD
    session.commit()



# create()
# read()
# update()
# delete()