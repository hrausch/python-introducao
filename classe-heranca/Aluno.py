class Pessoa:
	nomecompleto = ""
	cpf = ""

	def __init__(self):
		print("Criou uma Pessoa")

	# def __init__(self, nome, cpf):
	# 	self.nomecompleto = nome
	# 	self.cpf = cpf
	def mostrarNome(self):
		print("Nome (classe Pessoa): " + self.nomecompleto)


class Aluno (Pessoa):
	matricula = ""
	idade = ""
	genero = ""
	curso = ""

	def __init__(self):
		print("Criou um Aluno")

	def mostrarNome(self):
		print("Nome (classe Aluno): " + self.nomecompleto)


class TecnicoInfo(Aluno):

	anoFormatura = ""

	def __init__(self):
		print("Criou o tecnico")
