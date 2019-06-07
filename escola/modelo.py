import os
from peewee import *

arq = "aluno.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db
class Aluno(BaseModel):
	nome = CharField()

class Disciplina(BaseModel):
	nome = CharField()

class AlunoDisciplina(BaseModel):
	aluno = ForeignKeyField(Aluno)
	disciplina = ForeignKeyField(Disciplina)

if __name__ == "__main__":
	arq = "aluno.db"
	if os.path.exists(arq):
		os.remove(arq)

	try:
		db.connect()
		db.create_tables([Aluno, Disciplina, AlunoDisciplina])

	except OperationError as erro:
		print("erro ao criar as tabelas: "+str(erro))

	print("teste do animal")
	a1 = Animal(nome_dono="Gustavo", tipo_animal="cachorro", raca="linguicinha", nome_animal="Sarchixa")
	a1.save()
	print(a1)
	print("teste da consulta")
	c1 = Consulta(data="2019-06-05", servico="Consulta", horario="14:00", animal=a1, confirma="sim", myID="3425576687sdf436")
	

	todos = Animal.select()
	for i in todos:
		print(i)