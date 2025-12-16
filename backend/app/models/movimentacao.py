from uuid import uuid4
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base



class Movimentacao(Base):
    __tablename__ = "movimentacoes"
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid4()))
    produto_id = Column(String(36), ForeignKey("produtos.id"), nullable=False)
    produto_nome = Column(String(100), nullable=False)

    tipo = Column(String(10), nullable=False)  # entrada | saida
    quantidade = Column(Integer, nullable=False)

    data_movimentacao = Column(DateTime, default=datetime.utcnow)

    responsavel = Column(String(100), nullable=True)
    observacoes = Column(String(255), nullable=True)
    documento = Column(String(100), nullable=True)

    produto = relationship("Produto", back_populates="movimentacoes")
