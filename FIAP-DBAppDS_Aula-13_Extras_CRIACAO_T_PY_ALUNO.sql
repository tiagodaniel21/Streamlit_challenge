DROP TABLE T_PY_ALUNO;
CREATE TABLE T_PY_ALUNO (
    id NUMBER GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR2(100),
    idade NUMBER,
    endereco VARCHAR2(200),
    curso VARCHAR2(50)
);


ALTER TABLE T_PY_ALUNO ADD CONSTRAINT PK_PY_ALUNO PRIMARY KEY (id);


INSERT INTO T_PY_ALUNO (nome, idade, endereco, curso)
SELECT 'João Silva', 20, 'Rua A, 123', 'Engenharia' FROM DUAL UNION ALL
SELECT 'Maria Santos', 22, 'Avenida B, 456', 'Medicina' FROM DUAL UNION ALL
SELECT 'Pedro Souza', 19, 'Praça C, 789', 'Direito' FROM DUAL UNION ALL
SELECT 'Ana Oliveira', 21, 'Estrada D, 101', 'Arquitetura' FROM DUAL UNION ALL
SELECT 'Lucas Almeida', 23, 'Rua E, 234', 'Administração' FROM DUAL UNION ALL
SELECT 'Isabela Ferreira', 20, 'Avenida F, 567', 'Psicologia' FROM DUAL UNION ALL
SELECT 'Rafael Gonçalves', 24, 'Praça G, 890', 'Ciência da Computação' FROM DUAL UNION ALL
SELECT 'Larissa Rodrigues', 19, 'Estrada H, 111', 'Enfermagem' FROM DUAL UNION ALL
SELECT 'Gustavo Costa', 21, 'Rua I, 345', 'Economia' FROM DUAL UNION ALL
SELECT 'Fernanda Martins', 22, 'Avenida J, 678', 'Letras' FROM DUAL;

COMMIT;

SELECT * FROM T_PY_ALUNO;