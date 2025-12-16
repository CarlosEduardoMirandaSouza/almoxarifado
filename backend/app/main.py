from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.utils.error_handler import add_exception_handlers

from routers.produto import router as produto_router
from routers.movimentacao import router as movimentacao_router
from routers.requisicao import router as requisicao_router  # <-- ADICIONADO

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

# Instância da aplicação
app = FastAPI(title="API Almoxarifado")

# Libera CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra tratadores de erro
add_exception_handlers(app)

# Registra as rotas da API
app.include_router(produto_router)
app.include_router(movimentacao_router)
app.include_router(requisicao_router)  # <-- ADICIONADO
