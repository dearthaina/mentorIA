from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from database import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True)
    ra = Column(String(20), unique=True, nullable=False)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    data_cadastro = Column(DateTime, server_default=func.now())


class Documento(Base):
    __tablename__ = "documento"

    id_documento = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=False)
    nome_arquivo = Column(String(255), nullable=False)
    caminho_arquivo = Column(String(500), nullable=False)
    data_upload = Column(DateTime, server_default=func.now())