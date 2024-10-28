CREATE DATABASE Unifeob;

USE Unifeob;

CREATE TABLE professor (
    idprofessor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    matricula VARCHAR(20),
    curso VARCHAR(100),
    turma VARCHAR(20),
    modulo INT
);

CREATE TABLE universidade (
    iduniversidade INT AUTO_INCREMENT PRIMARY KEY,
    nome_aluno VARCHAR(100),
    ra VARCHAR(20),
    curso VARCHAR(100),
    turma VARCHAR(20),
    disciplina VARCHAR(100),
    modulo INT,
    semestre INT,
    predio VARCHAR(100),
    sala VARCHAR(50)
);

CREATE TABLE curso (
    idcurso INT AUTO_INCREMENT PRIMARY KEY,
    nomeCurso VARCHAR(100)
);

CREATE TABLE aplicativo (
    idaplicativo INT AUTO_INCREMENT PRIMARY KEY,
    localizacao VARCHAR(100)
);

CREATE TABLE sala (
    idsala INT AUTO_INCREMENT PRIMARY KEY,
    curso VARCHAR(100),
    periodo VARCHAR(20),
    localizacao VARCHAR(100),
    curso_idcurso INT,
    aplicativo_idaplicativo INT,
    FOREIGN KEY (curso_idcurso) REFERENCES curso(idcurso),
    FOREIGN KEY (aplicativo_idaplicativo) REFERENCES aplicativo(idaplicativo)
);

CREATE TABLE materia (
    idmateria INT AUTO_INCREMENT PRIMARY KEY,
    modulo INT,
    curso_idcurso INT,
    FOREIGN KEY (curso_idcurso) REFERENCES curso(idcurso)
);

CREATE TABLE aula (
    idaula INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    horario TIME,
    idprofessor INT,
    predio VARCHAR(100),
    sala VARCHAR(50),
    idmateria INT,
    status_presenca VARCHAR(50),
    FOREIGN KEY (idprofessor) REFERENCES professor(idprofessor),
    FOREIGN KEY (idmateria) REFERENCES materia(idmateria)
);

CREATE TABLE aluno (
    idaluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    ra VARCHAR(20),
    curso VARCHAR(100),
    turma VARCHAR(20),
    periodo VARCHAR(20),
    semestre INT,
    modulo INT,
	disciplinas VARCHAR(100),
    curso_idcurso INT,
    aplicativo_idaplicativo INT,
    FOREIGN KEY (curso_idcurso) REFERENCES curso(idcurso),
    FOREIGN KEY (aplicativo_idaplicativo) REFERENCES aplicativo(idaplicativo)
);

CREATE TABLE registro_presenca (
    idregistro INT AUTO_INCREMENT PRIMARY KEY,
    idaluno INT,
    idaula INT,
    data_leitura DATE,
    horario_leitura TIME,
    FOREIGN KEY (idaluno) REFERENCES aluno(idaluno),
    FOREIGN KEY (idaula) REFERENCES aula(idaula)
);

INSERT INTO professor (nome, matricula, curso, turma, modulo) 
VALUES ('João Silva', 'P123', 'Engenharia', 'T1', 1),
       ('Ana Costa', 'P456', 'Direito', 'T2', 2);

INSERT INTO universidade (nome_aluno, ra, curso, turma, disciplina, modulo, semestre, predio, sala) 
VALUES ('Carlos Santos', '12345', 'Engenharia', 'T1', 'Matemática', 1, 1, 'Bloco A', '101'),
       ('Marina Souza', '67890', 'Direito', 'T2', 'História', 2, 3, 'Bloco B', '203');

INSERT INTO aluno (nome, ra, curso, turma, periodo, semestre, modulo) 
VALUES ('Carlos Santos', '12345', 'Engenharia', 'T1', 'Noturno', 1, 1),
       ('Marina Souza', '67890', 'Direito', 'T2', 'Diurno', 3, 2);

INSERT INTO curso (nomeCurso) 
VALUES ('Engenharia'), 
       ('Direito');
       
INSERT INTO aula (data, horario, idprofessor, predio, sala, status_presenca) 
VALUES ('2024-10-02', '08:00:00', 1, 'Bloco A', '101', 'Presente'),
       ('2024-10-02', '10:00:00', 2, 'Bloco B', '203', 'Ausente');

INSERT INTO aplicativo (localizacao) 
VALUES ('Campus Norte'), 
       ('Campus Sul');

INSERT INTO materia (modulo, curso_idcurso) 
VALUES (1, 1), 
       (2, 2);
       
INSERT INTO registro_presenca (idaluno, data_leitura, horario_leitura) 
VALUES (1, '2024-10-03', '08:05:00'),
       (2, '2024-10-03', '10:10:00');
	
    
    SELECT * FROM ALUNO