import bcrypt

def gerar_hash(senha: str) -> str:
    senha_bytes = senha.encode("utf-8")
    salt = bcrypt.gensalt()
    
    return bcrypt.hashpw(senha_bytes, salt).decode("utf-8")

def verificar_senha(senha: str, senha_hash: str) -> bool:
    senha_bytes = senha.encode("utf-8")
    hash_bytes = senha_hash.encode("utf-8")

    return bcrypt.checkpw(senha_bytes, hash_bytes)