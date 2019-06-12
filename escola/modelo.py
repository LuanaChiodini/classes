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
	alunos = ManyToManyField(Aluno)

if __name__ == "__main__":
	arq = "aluno.db"
	if os.path.exists(arq):
		os.remove(arq)

	try:
		db.connect()
		db.create_tables([Aluno, Disciplina, Aluno.disciplinas.get_through_model()])

	except OperationError as erro:
		print("erro ao criar as tabelas: "+str(erro))

	joao = Aluno.create(nome="João")
	ingles = Disciplina.create(nome="Inglês")
	espanhol = Disciplina.create(nome="Espanhol")
	joao.disciplinas.add([ingles, espanhol])

	maria = Aluno.create(nome="Maria")
	espanhol.alunos.add(maria)

	todos = Disciplina.select()
	for disciplina in todos:
		print("quem cursa a disciplina:" + disciplina.nome)
		for aluno in disciplina.alunos:
			print(aluno.nome)

	print("disciplinas de joão:")
	for disciplina in joao.disciplinas:
		print(disciplina.nome)