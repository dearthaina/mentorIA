from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Usuario, Documento
app = FastAPI()


@app.get("/")
def raiz():
    return {"mensagem": "API MentorIA funcionando!"}


@app.post("/usuarios")
def criar_usuario(
    ra: str,
    nome: str,
    email: str,
    senha_hash: str,
    db: Session = Depends(get_db)
):
    usuario = Usuario(
        ra=ra,
        nome=nome,
        email=email,
        senha_hash=senha_hash
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return {
        "id_usuario": usuario.id_usuario,
        "ra": usuario.ra,
        "nome": usuario.nome,
        "email": usuario.email
    }
@app.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()

    return [
        {
            "id_usuario": usuario.id_usuario,
            "ra": usuario.ra,
            "nome": usuario.nome,
            "email": usuario.email
        }
        for usuario in usuarios
    ]
@app.get("/usuarios/{id_usuario}")
def buscar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(
        Usuario.id_usuario == id_usuario
    ).first()

    if not usuario:
        return {"mensagem": "Usuário não encontrado"}

    return {
        "id_usuario": usuario.id_usuario,
        "ra": usuario.ra,
        "nome": usuario.nome,
        "email": usuario.email
    }
@app.put("/usuarios/{id_usuario}")
def atualizar_usuario(
    id_usuario: int,
    ra: str,
    nome: str,
    email: str,
    senha_hash: str,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id_usuario == id_usuario
    ).first()

    if not usuario:
        return {"mensagem": "Usuário não encontrado"}

    usuario.ra = ra
    usuario.nome = nome
    usuario.email = email
    usuario.senha_hash = senha_hash

    db.commit()
    db.refresh(usuario)

    return {
        "id_usuario": usuario.id_usuario,
        "ra": usuario.ra,
        "nome": usuario.nome,
        "email": usuario.email
    }
@app.delete("/usuarios/{id_usuario}")
def deletar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(
        Usuario.id_usuario == id_usuario
    ).first()

    if not usuario:
        return {"mensagem": "Usuário não encontrado"}

    db.delete(usuario)
    db.commit()

    return {"mensagem": "Usuário deletado com sucesso"}






@app.post("/documentos")
def criar_documento(
    id_usuario: int,
    nome_arquivo: str,
    caminho_arquivo: str,
    db: Session = Depends(get_db)
):
    documento = Documento(
        id_usuario=id_usuario,
        nome_arquivo=nome_arquivo,
        caminho_arquivo=caminho_arquivo
    )

    db.add(documento)
    db.commit()
    db.refresh(documento)

    return {
        "id_documento": documento.id_documento,
        "id_usuario": documento.id_usuario,
        "nome_arquivo": documento.nome_arquivo,
        "caminho_arquivo": documento.caminho_arquivo
    }

@app.get("/documentos")
def listar_documentos(db: Session = Depends(get_db)):
    documentos = db.query(Documento).all()

    return [
        {
            "id_documento": documento.id_documento,
            "id_usuario": documento.id_usuario,
            "nome_arquivo": documento.nome_arquivo,
            "caminho_arquivo": documento.caminho_arquivo
        }
        for documento in documentos
    ]
@app.get("/documentos/{id_documento}")
def buscar_documento(
    id_documento: int,
    db: Session = Depends(get_db)
):
    documento = db.query(Documento).filter(
        Documento.id_documento == id_documento
    ).first()

    if not documento:
        return {"mensagem": "Documento não encontrado"}

    return {
        "id_documento": documento.id_documento,
        "id_usuario": documento.id_usuario,
        "nome_arquivo": documento.nome_arquivo,
        "caminho_arquivo": documento.caminho_arquivo
    }
@app.put("/documentos/{id_documento}")
def atualizar_documento(
    id_documento: int,
    id_usuario: int,
    nome_arquivo: str,
    caminho_arquivo: str,
    db: Session = Depends(get_db)
):
    documento = db.query(Documento).filter(
        Documento.id_documento == id_documento
    ).first()

    if not documento:
        return {"mensagem": "Documento não encontrado"}

    documento.id_usuario = id_usuario
    documento.nome_arquivo = nome_arquivo
    documento.caminho_arquivo = caminho_arquivo

    db.commit()
    db.refresh(documento)

    return {
        "id_documento": documento.id_documento,
        "id_usuario": documento.id_usuario,
        "nome_arquivo": documento.nome_arquivo,
        "caminho_arquivo": documento.caminho_arquivo
    }

@app.delete("/documentos/{id_documento}")
def deletar_documento(
    id_documento: int,
    db: Session = Depends(get_db)
):
    documento = db.query(Documento).filter(
        Documento.id_documento == id_documento
    ).first()

    if not documento:
        return {"mensagem": "Documento não encontrado"}

    db.delete(documento)
    db.commit()

    return {"mensagem": "Documento deletado com sucesso"}