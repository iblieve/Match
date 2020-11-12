import os
from sqlalchemy import Column, String, create_engine, Integer, Float
from sqlalchemy.orm import sessionmaker
from models import Tpoint


def create_list(p_config=None):
    """

    :param p_config:
    :return:
    """
    url = f'mysql+pymysql://{p_config.DB_USER}:{p_config.DB_PASSWORD}@{p_config.DB_HOST}:{p_config.DB_PORT}/{p_config.DB_INSTANCE_NAME}?charset={p_config.DB_CHARSET}'
    engine = create_engine(url)
    # engine = create_engine('mysql+pymysql://root:123456@localhost:3306/mysql?charset=utf8')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    results = session.query(Tpoint).all()
    session.close()
    return results