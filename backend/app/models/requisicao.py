from uuid import uuid4
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Requisicao(Base):
    __tablename__ = "requisicoes"
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    produto_id = Column(String(36), ForeignKey("produtos.id"), nullable=False)

    quantidade_solicitada = Column(Integer, nullable=False)
    estoque_atual = Column(Integer, nullable=True)
    estoque_minimo = Column(Integer, nullable=True)
    prioridade = Column(String(20), nullable=True)
    status = Column(String(20), nullable=False, default="pendente")
    justificativa = Column(String(255), nullable=True)
    observacoes = Column(String(255), nullable=True)
    created_date = Column(DateTime, default=datetime.utcnow)

    produto = relationship("Produto", back_populates="requisicoes")
