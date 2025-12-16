from uuid import uuid4
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Produto(Base):
    __tablename__ = "produtos"
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid4()))
    nome = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=True)
    unidade_medida = Column(String(20), nullable=True)

    estoque_atual = Column(Integer, nullable=False, default=0)
    estoque_minimo = Column(Integer, nullable=False, default=0)
    estoque_maximo = Column(Integer, nullable=True)
    custo_unitario = Column(Float, nullable=True)

    status = Column(String(20), nullable=False, default="normal")  # normal | alerta | critico

    movimentacoes = relationship("Movimentacao", back_populates="produto", cascade="all, delete-orphan")
    requisicoes = relationship("Requisicao", back_populates="produto", cascade="all, delete-orphan")
