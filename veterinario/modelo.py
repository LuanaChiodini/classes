import peewee, os

db = peewee.SqliteDatabase("animal.db")

class Animal(peewee.Model):
	nome_dono = peewee.CharField()
	tipo_animal = peewee.CharField()
	raca = peewee.CharField()
	nome_animal = peewee.CharField()

	class Meta():
		database = db

		def __str__(self):
			return self.tipo_animal, self.raca, self.nome_dono, self.nome_animal

class Consulta(peewee.Model):
	data = peewee.CharField()
	servidor = peewee.CharField()
	horario = peewee.CharField()
	animal = peewee.ForeignKeyField(Animal)
	confirma = peewee.CharField()
	myID = peewee.CharField()

	class Meta():
		database = db

	def __str__(self):
		return self.servico, self.data, self.horario, self.confirma, self.myID, str(self.animal)

if __name__ == "__main__":
	arq = "animal.db"
	if os.path.exists(arq):
		os.remove(arq)

	try:
		db.connect()
		db.create_tables([Animal, Consulta])

	except peewee.OperationError as erro:
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