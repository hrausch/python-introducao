#sudo apt-get install pip3

#pip3 install pymysql sqlalchemy

import sqlalchemy as db


engine = db.create_engine("mysql+pymysql://root:root@localhost/company2?charset=utf8mb4")
connection = engine.connect()


metadata = db.MetaData()

employee = db.Table('EMPLOYEE', metadata, autoload=True, autoload_with=engine)

print(employee.columns)





