-- =========================================
-- USUÁRIOS
-- =========================================

INSERT INTO usuario (ra, nome, email, senha_hash)
VALUES
    ('20260001', 'Cleonice Abreu', 'cleonice@email.com', 'HASH_DE_TESTE_001'),
    ('20260002', 'Mariana Menezes', 'mariana@email.com', 'HASH_DE_TESTE_002');

-- =========================================
-- DOCUMENTOS
-- =========================================

INSERT INTO documento (id_usuario, nome_arquivo, caminho_arquivo)
VALUES
    (1, 'Redes_de_Computadores.pdf', '/documentos/redes_de_computadores.pdf'),
    (1, 'Banco_de_Dados.pdf', '/documentos/banco_de_dados.pdf'),
    (2, 'Programacao_Python.pdf', '/documentos/programacao_python.pdf');

-- =========================================
-- CONVERSAS
-- =========================================

INSERT INTO conversa (id_usuario, id_documento, titulo)
VALUES
    (1, 1, 'Dúvidas sobre TCP/IP'),
    (1, 1, 'Revisão para prova de Redes'),
    (1, 2, 'Dúvidas sobre SQL'),
    (2, 3, 'Introdução ao Python');

-- =========================================
-- MENSAGENS
-- =========================================

INSERT INTO mensagem (id_conversa, origem, conteudo)
VALUES
    (1, 'usuario', 'O que significa TCP?'),
    (1, 'ia', 'TCP é um protocolo responsável pela transmissão confiável de dados em uma rede.'),

    (1, 'usuario', 'E qual é a diferença entre TCP e UDP?'),
    (1, 'ia', 'TCP prioriza confiabilidade e controle da transmissão, enquanto UDP prioriza menor overhead e velocidade.'),

    (2, 'usuario', 'Quais assuntos de redes devo revisar para a prova?'),
    (2, 'ia', 'Você pode revisar os principais protocolos, modelos de rede, endereçamento IP e conceitos de transporte.'),

    (3, 'usuario', 'O que é uma chave estrangeira?'),
    (3, 'ia', 'Uma chave estrangeira é um campo que referencia uma chave de outra tabela, permitindo estabelecer um relacionamento entre elas.'),

    (4, 'usuario', 'O que é uma lista em Python?'),
    (4, 'ia', 'Uma lista é uma estrutura de dados que permite armazenar vários valores em uma única variável.');