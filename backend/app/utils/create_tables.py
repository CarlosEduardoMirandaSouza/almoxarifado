import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.database import Base, engine
from app.models.produto import Produto
from app.models.movimentacao import Movimentacao
from app.models.requisicao import Requisicao

print("🔧 Criando tabelas no MySQL...")
Base.metadata.create_all(bind=engine)
print("✅ Tabelas criadas com sucesso!")
