CREATE TABLE usuario (
  id_usuario SERIAL PRIMARY KEY,
  ra VARCHAR(20) UNIQUE NOT NULL,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(150) UNIQUE NOT NULL,
  senha_hash VARCHAR(255) NOT NULL,
  data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE documento (
  id_documento SERIAL PRIMARY KEY,
  id_usuario INTEGER NOT NULL,
  nome_arquivo VARCHAR(255) NOT NULL,
  caminho_arquivo VARCHAR(500) NOT NULL,
  data_upload TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT fk_documento_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

CREATE TABLE conversa (
  id_conversa SERIAL PRIMARY KEY,
  id_usuario INTEGER NOT NULL,
  id_documento INTEGER NOT NULL,
  titulo VARCHAR(150) NOT NULL,
  data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT fk_conversa_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
  CONSTRAINT fk_conversa_documento FOREIGN KEY (id_documento) REFERENCES documento(id_documento)
);

CREATE TABLE mensagem (
  id_mensagem SERIAL PRIMARY KEY,
  id_conversa INTEGER NOT NULL,
  origem VARCHAR(20) NOT NULL,
  conteudo TEXT NOT NULL,
  data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT fk_mensagem_conversa FOREIGN KEY (id_conversa) REFERENCES conversa(id_conversa),
  CONSTRAINT chk_origem_mensagem CHECK (origem IN ('usuario', 'ia'))
);