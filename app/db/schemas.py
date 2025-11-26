from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from .config import BASE


class Product(BASE):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Tag(BASE):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tag = Column(String, index=True, nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
