from utils.mo_utils import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    BIGINT,
    DateTime,
    String,
    Float,
    Text,
    JSON
)

import datetime

def current_timestamp():
    return int(time.time())

class BaseMixin:
    """model的基类,所有model都必须继承"""
    # __abstract__ = True

    # id = Column(String(255), primary_key=True)
    # created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    # updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now, index=True)
    # deleted_at = Column(DateTime)

    id = Column(BIGINT, primary_key=True)
    created_at = Column(BIGINT, nullable=False, default=current_timestamp)
    updated_at = Column(BIGINT, nullable=False, default=current_timestamp, onupdate=current_timestamp, index=True)
