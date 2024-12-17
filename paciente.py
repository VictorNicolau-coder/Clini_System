class paciente:
    def __init__(self, id_paciente, nome, idade, telefone, endereco):
        self.id_paciente = id_paciente
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.endereco = endereco

    def imprime_ficha(self):
        print("============================")
        print("ID do Paciente:", self.id_paciente)
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Telefone:", self.telefone)
        print("Endereço:", self.endereco)
        print("============================")
