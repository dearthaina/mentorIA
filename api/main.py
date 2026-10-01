from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Usuario, Documento, Conversa, Mensagem

app = FastAPI()


@app.get("/")
def raiz():
    return {"mensagem": "API MentorIA funcionando!"}


# =========================
# USUÁRIOS
# =========================

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
def buscar_usuario(
    id_usuario: int,
    db: Session = Depends(get_db)
):
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
def deletar_usuario(
    id_usuario: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id_usuario == id_usuario
    ).first()

    if not usuario:
        return {"mensagem": "Usuário não encontrado"}

    db.delete(usuario)
    db.commit()

    return {"mensagem": "Usuário deletado com sucesso"}


# =========================
# DOCUMENTOS
# =========================

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


# =========================
# CONVERSAS
# =========================

@app.post("/conversas")
def criar_conversa(
    id_usuario: int,
    id_documento: int,
    titulo: str,
    db: Session = Depends(get_db)
):
    conversa = Conversa(
        id_usuario=id_usuario,
        id_documento=id_documento,
        titulo=titulo
    )

    try:
        db.add(conversa)
        db.commit()
        db.refresh(conversa)

        return {
            "id_conversa": conversa.id_conversa,
            "id_usuario": conversa.id_usuario,
            "id_documento": conversa.id_documento,
            "titulo": conversa.titulo,
            "data_criacao": conversa.data_criacao,
            "data_atualizacao": conversa.data_atualizacao
        }

    except Exception as erro:
        db.rollback()

        return {
            "erro": "Não foi possível criar a conversa",
            "detalhes": str(erro)
        }


@app.get("/conversas")
def listar_conversas(db: Session = Depends(get_db)):
    conversas = db.query(Conversa).all()

    return [
        {
            "id_conversa": conversa.id_conversa,
            "id_usuario": conversa.id_usuario,
            "id_documento": conversa.id_documento,
            "titulo": conversa.titulo,
            "data_criacao": conversa.data_criacao,
            "data_atualizacao": conversa.data_atualizacao
        }
        for conversa in conversas
    ]


@app.get("/conversas/{id_conversa}")
def buscar_conversa(
    id_conversa: int,
    db: Session = Depends(get_db)
):
    conversa = db.query(Conversa).filter(
        Conversa.id_conversa == id_conversa
    ).first()

    if not conversa:
        return {"mensagem": "Conversa não encontrada"}

    return {
        "id_conversa": conversa.id_conversa,
        "id_usuario": conversa.id_usuario,
        "id_documento": conversa.id_documento,
        "titulo": conversa.titulo,
        "data_criacao": conversa.data_criacao,
        "data_atualizacao": conversa.data_atualizacao
    }

@app.put("/conversas/{id_conversa}")
def atualizar_conversa(
    id_conversa: int,
    id_usuario: int,
    id_documento: int,
    titulo: str,
    db: Session = Depends(get_db)
):
    conversa = db.query(Conversa).filter(
        Conversa.id_conversa == id_conversa
    ).first()

    if not conversa:
        return {"mensagem": "Conversa não encontrada"}

    conversa.id_usuario = id_usuario
    conversa.id_documento = id_documento
    conversa.titulo = titulo

    db.commit()
    db.refresh(conversa)

    return {
        "id_conversa": conversa.id_conversa,
        "id_usuario": conversa.id_usuario,
        "id_documento": conversa.id_documento,
        "titulo": conversa.titulo,
        "data_criacao": conversa.data_criacao,
        "data_atualizacao": conversa.data_atualizacao
    }

@app.delete("/conversas/{id_conversa}")
def deletar_conversa(
    id_conversa: int,
    db: Session = Depends(get_db)
):
    conversa = db.query(Conversa).filter(
        Conversa.id_conversa == id_conversa
    ).first()

    if not conversa:
        return {"mensagem": "Conversa não encontrada"}

    db.delete(conversa)
    db.commit()

    return {"mensagem": "Conversa deletada com sucesso"}


@app.post("/mensagens")
def criar_mensagem(
    id_conversa: int,
    origem: str,
    conteudo: str,
    db: Session = Depends(get_db)
):
    mensagem = Mensagem(
        id_conversa=id_conversa,
        origem=origem,
        conteudo=conteudo
    )

    try:
        db.add(mensagem)
        db.commit()
        db.refresh(mensagem)

        return {
            "id_mensagem": mensagem.id_mensagem,
            "id_conversa": mensagem.id_conversa,
            "origem": mensagem.origem,
            "conteudo": mensagem.conteudo,
            "data_envio": mensagem.data_envio
        }

    except Exception as erro:
        db.rollback()
        return {
            "erro": "Não foi possível criar a mensagem",
            "detalhes": str(erro)
        }


@app.get("/mensagens")
def listar_mensagens(db: Session = Depends(get_db)):
    mensagens = db.query(Mensagem).all()

    return [
        {
            "id_mensagem": mensagem.id_mensagem,
            "id_conversa": mensagem.id_conversa,
            "origem": mensagem.origem,
            "conteudo": mensagem.conteudo,
            "data_envio": mensagem.data_envio
        }
        for mensagem in mensagens
    ]


@app.get("/mensagens/{id_mensagem}")
def buscar_mensagem(
    id_mensagem: int,
    db: Session = Depends(get_db)
):
    mensagem = db.query(Mensagem).filter(
        Mensagem.id_mensagem == id_mensagem
    ).first()

    if not mensagem:
        return {"mensagem": "Mensagem não encontrada"}

    return {
        "id_mensagem": mensagem.id_mensagem,
        "id_conversa": mensagem.id_conversa,
        "origem": mensagem.origem,
        "conteudo": mensagem.conteudo,
        "data_envio": mensagem.data_envio
    }


@app.put("/mensagens/{id_mensagem}")
def atualizar_mensagem(
    id_mensagem: int,
    id_conversa: int,
    origem: str,
    conteudo: str,
    db: Session = Depends(get_db)
):
    mensagem = db.query(Mensagem).filter(
        Mensagem.id_mensagem == id_mensagem
    ).first()

    if not mensagem:
        return {"mensagem": "Mensagem não encontrada"}

    mensagem.id_conversa = id_conversa
    mensagem.origem = origem
    mensagem.conteudo = conteudo

    try:
        db.commit()
        db.refresh(mensagem)

        return {
            "id_mensagem": mensagem.id_mensagem,
            "id_conversa": mensagem.id_conversa,
            "origem": mensagem.origem,
            "conteudo": mensagem.conteudo,
            "data_envio": mensagem.data_envio
        }

    except Exception as erro:
        db.rollback()
        return {
            "erro": "Não foi possível atualizar a mensagem",
            "detalhes": str(erro)
        }


@app.delete("/mensagens/{id_mensagem}")
def deletar_mensagem(
    id_mensagem: int,
    db: Session = Depends(get_db)
):
    mensagem = db.query(Mensagem).filter(
        Mensagem.id_mensagem == id_mensagem
    ).first()

    if not mensagem:
        return {"mensagem": "Mensagem não encontrada"}

    try:
        db.delete(mensagem)
        db.commit()

        return {"mensagem": "Mensagem deletada com sucesso"}

    except Exception as erro:
        db.rollback()
        return {
            "erro": "Não foi possível deletar a mensagem",
            "detalhes": str(erro)
        }