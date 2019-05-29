class Aluno():
	def __init__(self, nome, data_nascimento, matricula, turma):
		self.nome = nome
		self.data_nascimento = data_nascimento
		self.matricula = matricula
		self.turma = turma

class Professor():
	def __init__(self, nome, data_nascimento, cpf, atuacao):
		self.nome = nome
		self.data_nascimento = data_nascimento
		self.cpf = cpf
		self.atuacao = atuacao

class Projeto():
	def __init__(self, nome, ano, lista_alunos, lista_orientadores):
		self.nome = nome
		self.ano = ano
		self.lista_alunos = lista_alunos
		self.lista_orientadores = lista_orientadores
