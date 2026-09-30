from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Usuario

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