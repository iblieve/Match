#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from sqlalchemy import Column, String, create_engine, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from models import Tpoint
from app.main.models.XAddress import XAddress

def create_list(p_config=None):
    """

    :param p_config:
    :return:
    """
    url = f'mysql+pymysql://{p_config.DB_USER}:{p_config.DB_PASSWORD}@{p_config.DB_HOST}:{p_config.DB_PORT}/{p_config.DB_INSTANCE_NAME}?charset={p_config.DB_CHARSET}'
    # NOTE
    # NOTE https://blog.csdn.net/ypgsh/article/details/102516720
    # NOTE
    # NOTE 在以默认的方法 create_engine 时（如下），就会创建一个带连接池的引擎。
    # NOTE engine = create_engine('mysql+mysqldb://root:password@127.0.0.1:3306/dbname')
    # NOTE 在此情况下，当你使用了session后就算显式地调用 session.close()，也不能把连接关闭。连接会由 QueuePool连接池进行管理并复用。
    # NOTE
    # NOTE 这种特性在一般情况下并不会有问题，不过当数据库服务器因为一些原因进行了重启的话。最初保持的数据库连接就失效了。
    # NOTE 随后进行的 session.query() 等方法就会抛出异常导致程序出错。
    # NOTE
    # NOTE 如果想禁用 SQLAlchemy 提供的数据库连接池，只需要在调用 create_engine 是指定连接池为 NullPool，
    # NOTE SQLAlchemy 就会在执行 session.close()后立刻断开数据库连接。当然，如果session对象被析构但是没有被调用session.close()，
    # NOTE 则数据库连接不会被断开，直到程序终止。
    # NOTE
    engine = create_engine(url, poolclass=NullPool)
    # engine = create_engine('mysql+pymysql://root:123456@localhost:3306/mysql?charset=utf8')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    #results = session.query(Tpoint).all()
    results = session.query(XAddress).all()

    session.close()
    return results
