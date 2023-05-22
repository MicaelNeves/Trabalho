	
	CREATE TABLE "Disciplina"(
	"CodDisciplina" varchar(11) NOT NULL PRIMARY KEY,
	"Nome" varchar(255) NOT NULL,
	"CodCurso" varchar(100) NOT NULL
	);
	
	CREATE TABLE "Matrícula"(
	"NroMatricula" varchar(11) NOT NULL PRIMARY KEY,
	"CodDisciplina" varchar(11) NOT NULL,
	"Semestre" varchar(11) NOT NULL,
	"Ano" int NOT NULL,
	"Notas" int NOT NULL,
	"Nro Faltas" int NOT NULL default 0,
		
	CONSTRAINT fk_disciplina
	FOREIGN KEY("CodDisciplina")
	REFERENCES "Disciplina"("CodDisciplina")
	
	);
	
	CREATE TABLE "Alunos"(
	"NroMatricula" varchar(11) NOT NULL,
	"CPF" varchar(11) NOT NULL,
	"Nome" varchar(255) NOT NULL,
	"Nome Endereço" varchar(255),
	"Telefone" int NOT NULL,
	"Ano de Nascimento" varchar(10),
		
	CONSTRAINT fk_matricula
	FOREIGN KEY("NroMatricula")
	REFERENCES "Matrícula"("NroMatricula")
	);
	
	

	
	