from sqlalchemy import Column, String, create_engine, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Address(Base):
    __tablename__ = 'tpoint'
    row_id = Column(Integer, primary_key=True)
    location_id = Column(String(20))
    province_name = Column(String(100))
    city_name = Column(String(100))
    district_name = Column(String(100))
    town_name = Column(String(100))
    location_name = Column(String(200))
    address = Column(String(200))
    longitude = Column(Float)
    latitude = Column(Float)

    def __repr__(self):
        tpl = "Address(row_id={}, location_id={}, province_name={}, city_name={}, district_name={}, town_name={}, " \
              "location_name={}, address={}, longitude={}, latitude={}) "
        return tpl.format(self.row_id, self.location_id, self.province_name, self.city_name, self.district_name, self.town_name, self.location_name, self.address, self.longitude, self.latitude)


def create_list(dialect=None, driver=None, username=None, password=None, host='localhost', port=3306, database=None):
    # 初始化数据库连接:
    engine = create_engine(f'{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?charset=utf8')
    # engine = create_engine('mysql+pymysql://root:123456@localhost:3306/mysql?charset=utf8')
    DBSession = sessionmaker(bind=engine)

    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(Address).all()
    # 打印类型和对象的name属性:
    # print('type:', type(user))
    # print(user)
    # 关闭Session:
    session.close()
    return user


addr_list = create_list(dialect='mysql', driver='pymysql', username='root', password='123456', database='mysql')
#print(len(addr_list))


