# coding: utf-8
from sqlalchemy import Column, Float, Integer, MetaData, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata



class Tpoint(Base):
    __tablename__ = 'tpoint'

    row_id = Column(Integer, primary_key=True)
    location_id = Column(String(20), nullable=False)
    province_name = Column(String(30), nullable=False)
    city_name = Column(String(30), nullable=False)
    district_name = Column(String(30))
    town_name = Column(String(30))
    location_name = Column(String(300), nullable=False)
    address = Column(String(300), nullable=False)
    longitude = Column(Float(9, True), nullable=False)
    latitude = Column(Float(9, True), nullable=False)
