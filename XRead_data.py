import os
from sqlalchemy import Column, String, create_engine, Integer, Float
from sqlalchemy.orm import sessionmaker
from models import Tpoint


if os.getenv('DB_HOST') is not None:
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_INSTANCE_NAME = os.environ['DB_INSTANCE_NAME']
    DB_CHARSET = os.environ['DB_CHARSET']


def create_list(dialect=None, driver=None):
    # 初始化数据库连接:
    engine = create_engine(f'{dialect}+{driver}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_INSTANCE_NAME}?charset={DB_CHARSET}')
    # engine = create_engine('mysql+pymysql://root:123456@localhost:3306/mysql?charset=utf8')
    DBSession = sessionmaker(bind=engine)

    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(Tpoint).all()
    # 打印类型和对象的name属性:
    # print('type:', type(user))
    # print(user)
    # 关闭Session:
    session.close()
    return user


# addr_list = create_list(dialect='mysql', driver='pymysql')
# print(addr_list[0].row_id)





