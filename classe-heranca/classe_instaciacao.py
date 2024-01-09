'''
TODO : exemplo de construtor diferente
'''

class Pessoa:
	nomecompleto = ""
	cpf = ""

	def __init__(self):
		print("Criou uma Pessoa")


	def mostrarNome(self):
		print("Nome (classe Pessoa): " + self.nomecompleto)

# INSTANCIACAO DE OBJETOS
print("** Instanciando pessoa **")

pessoa1 = Pessoa()
pessoa1.nomecompleto = "Herbert"
pessoa1.mostrarNome()
print(pessoa1)
print(pessoa1.mostrarNome())
print(pessoa1.cpf)

print("** Nova instancia de pessoa **")

pessoa2 = Pessoa()
pessoa2.nomecompleto = "Rausch"
pessoa2.cpf = "111.111.111-11"
print(pessoa2)
print(pessoa2.mostrarNome())
print(pessoa2.cpf)

print("** Nova instancia de pessoa 2 **")

pessoa2 = Pessoa()
pessoa2.nomecompleto = "Fernandes"
print(pessoa2)
print(pessoa2.cpf)

print("** Copiando referencia **")

pessoa2 = pessoa1
print(pessoa2)
print(pessoa2.mostrarNome())