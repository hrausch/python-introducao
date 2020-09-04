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
		
		

pessoa1 = Pessoa()
pessoa1.nomecompleto = "Herbert"
pessoa1.mostrarNome()




aluno1 = Aluno()
aluno1.nomecompleto = "Herbert"
aluno1.mostrarNome()


tec1 = TecnicoInfo()
tec1.nomecompleto = "Herbert"
tec1.mostrarNome()


print(tec1)

tec2 = TecnicoInfo()
print(tec2)

tec1 = TecnicoInfo()
print(tec3)

