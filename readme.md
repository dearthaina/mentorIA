# MentorIA

O **MentorIA** é um projeto com o objetivo de criar uma plataforma de apoio aos estudos utilizando **Inteligência Artificial**.

A proposta é permitir que estudantes façam o upload de documentos de estudo, como PDFs, e possam interagir com o conteúdo por meio de uma conversa com a IA, facilitando a compreensão e revisão dos materiais.

O projeto está sendo desenvolvido inicialmente com foco em uma arquitetura baseada em **API + Banco de Dados**, com possibilidade de integração futura com a aplicação web e os serviços de Inteligência Artificial.

# Objetivo

O MentorIA busca facilitar o estudo a partir dos próprios materiais do aluno.

A ideia é que o estudante possa:

* Enviar materiais de estudo em PDF;
* Fazer perguntas sobre o conteúdo do documento;
* Manter uma conversa relacionada a cada documento;
* Consultar conversas anteriores;
* Solicitar explicações mais simples ou mais aprofundadas;
* Organizar documentos e conversas de estudo.

# Tecnologias

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Supabase
* Uvicorn
* Psycopg
* Git e GitHub

# Estrutura do projeto

```text
mentorIA/
│
├── api/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── security.py
│
├── database/
│   └── schema.sql
│
├── requirements.txt
├── .env
└── readme.md
```

# Configuração do ambiente

## 1. Clonar o projeto

```bash
git clone https://github.com/dearthaina/mentorIA.git
```

Depois, entre na pasta:

```bash
cd mentorIA
```

## 2. Criar o ambiente virtual

No Windows:

```powershell
python -m venv venv
```

## 3. Ativar o ambiente virtual

No PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

No Prompt de Comando:

```cmd
venv\Scripts\activate
```

## 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

# Configuração do banco de dados

A API utiliza a variável de ambiente `DATABASE_URL` para realizar a conexão com o PostgreSQL.

Na raiz do projeto, crie um arquivo chamado:

```text
.env
```

Adicione a URL de conexão fornecida pelo banco de dados:

```env
DATABASE_URL=sua_url_de_conexao
```

O arquivo `.env` contém informações de acesso ao banco de dados e não deve ser enviado para o GitHub.

# Executando a API

Entre na pasta `api`:

```powershell
cd api
```

Com o ambiente virtual ativado, execute:

```powershell
uvicorn main:app --reload
```

A API ficará disponível em:

```text
http://127.0.0.1:8000
```

# Swagger

O FastAPI disponibiliza automaticamente uma interface para testar os endpoints.

Acesse:

```text
http://127.0.0.1:8000/docs
```

No Swagger é possível realizar os testes de:

* criação;
* consulta;
* alteração;
* exclusão.

# Endpoints da API

## Usuários

| Método | Endpoint                 | Função            |
| ------ | ________________________ | _________________ |
| POST   | `/usuarios`              | Criar usuário     |
| GET    | `/usuarios`              | Listar usuários   |
| GET    | `/usuarios/{id_usuario}` | Consultar usuário |
| PUT    | `/usuarios/{id_usuario}` | Atualizar usuário |
| DELETE | `/usuarios/{id_usuario}` | Excluir usuário   |

## Documentos

| Método | Endpoint                     | Função              |
| ------ | _____________________________| ___________________ |
| POST   | `/documentos`                | Criar documento     |
| GET    | `/documentos`                | Listar documentos   |
| GET    | `/documentos/{id_documento}` | Consultar documento |
| PUT    | `/documentos/{id_documento}` | Atualizar documento |
| DELETE | `/documentos/{id_documento}` | Excluir documento   |

## Conversas

| Método | Endpoint                   | Função             |
| ------ | __________________________ | __________________ |
| POST   | `/conversas`               | Criar conversa     |
| GET    | `/conversas`               | Listar conversas   |
| GET    | `/conversas/{id_conversa}` | Consultar conversa |
| PUT    | `/conversas/{id_conversa}` | Atualizar conversa |
| DELETE | `/conversas/{id_conversa}` | Excluir conversa   |

## Mensagens

| Método | Endpoint                   | Função             |
| ------ | __________________________ | __________________ |
| POST   | `/mensagens`               | Criar mensagem     |
| GET    | `/mensagens`               | Listar mensagens   |
| GET    | `/mensagens/{id_mensagem}` | Consultar mensagem |
| PUT    | `/mensagens/{id_mensagem}` | Atualizar mensagem |
| DELETE | `/mensagens/{id_mensagem}` | Excluir mensagem   |

# Banco de dados

O banco de dados PostgreSQL possui as seguintes entidades principais:

* `usuario`
* `documento`
* `conversa`
* `mensagem`

Os relacionamentos principais são:

```text
usuario
   |
   +-- documento
   |      |
   |      +-- conversa
   |             |
   |             +-- mensagem
   |
   +-- conversa
```

O script de criação das tabelas está disponível em:

```text
database/schema.sql
```

# Desenvolvimento

O projeto está sendo desenvolvido de forma incremental, com a API preparada para futuras integrações com:

* aplicação web;
* serviços de Inteligência Artificial;
* processamento de documentos;
* autenticação e controle de acesso.

________________________________________________________________________________________________________________________________________________________________________