BEGIN TRANSACTION;
CREATE TABLE Pessoa (nome text, CPF integer, Telephone integer, email varchar, address varchar, necessity varchar);
INSERT INTO "Pessoa" VALUES('Anna',123456789011,48765432678,'ong@gmail.com','rua 1234','comida');
INSERT INTO "Pessoa" VALUES('Regis',0,'11-98765-4321','regis@email.com','Sao Paulo-SP','dinheiro');
INSERT INTO "Pessoa" VALUES('Aloisio',11111111111,'98765-4322','aloisio@email.com','Porto Alegre-RS','comida');
INSERT INTO "Pessoa" VALUES('Bruna',22222222222,'21-98765-4323','bruna@email.com','Rio de Janeiro-RJ','roupa');
INSERT INTO "Pessoa" VALUES('Matheus',33333333333,'11-98765-4324','matheus@email.com','Campinas-SP','comida');
INSERT INTO "Pessoa" VALUES('anna',192839049,4899933300,'anna@gmail.com','rua blablabla','comida');
COMMIT;
