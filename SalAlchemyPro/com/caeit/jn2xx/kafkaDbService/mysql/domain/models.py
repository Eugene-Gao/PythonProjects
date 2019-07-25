# coding: utf-8
from sqlalchemy import BigInteger, Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db = declarative_base()


class NzLlJbsx(db):
    __tablename__ = 'nz_ll_jbsx'

    dxbm = Column(String(20), primary_key=True)
    dxbm1 = Column(String(20), nullable=False)
    dxlm1 = Column(Integer, nullable=False)
    dxbm2 = Column(String(20), nullable=False)
    dxlm2 = Column(Integer, nullable=False)
    fx = Column(Integer, nullable=False)
    slsj = Column(BigInteger, nullable=False)


class NzLlKzsxIdirect(db):
    __tablename__ = 'nz_ll_kzsx_idirect'

    dxbm = Column(String(20), primary_key=True)
    tlqssj = Column(BigInteger)
    wtmc = Column(String(64))
    txsblx = Column(Integer)
    wxmc = Column(String(64))


class NzSbJbsx(db):
    __tablename__ = 'nz_sb_jbsx'

    dxbm = Column(String(20), primary_key=True)
    sbmc = Column(String(64), nullable=False)
    sblx = Column(Integer, nullable=False)
    jbxx = Column(String(256), nullable=False)
    kszt = Column(Integer, nullable=False)
    scck = Column(String(256), nullable=False)


class NzSbKzsxIosb(db):
    __tablename__ = 'nz_sb_kzsx_iosb'

    dxbm = Column(String(20), primary_key=True)
    qjbm = Column(String(20))
    glwlllbh = Column(String(20))
    mc = Column(String(20))
    bb = Column(String(20))


class NzWlptJbsx(db):
    __tablename__ = 'nz_wlpt_jbsx'

    dxbm = Column(String(20), primary_key=True)
    ptlb = Column(Integer)
    ptlx = Column(Integer, nullable=False)
    dxfl = Column(Integer)
    slsj = Column(BigInteger, nullable=False)


class NzWlptKzsxFj(db):
    __tablename__ = 'nz_wlpt_kzsx_fj'

    dxbm = Column(String(20), primary_key=True)
    ph = Column(String(16))
    jxh = Column(String(8), nullable=False)
    tdsx = Column(String(128))
    zbxh = Column(String(20))
