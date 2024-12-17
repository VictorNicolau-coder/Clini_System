class notafiscal:
    def __init__(self, id_nota, id_paciente, valor, data_emissao):
        self.id_nota = id_nota
        self.id_paciente = id_paciente
        self.valor = valor
        self.data_emissao = data_emissao

    def emitir(self):
        print("============================")
        print("Nota fiscal emitida com sucesso!")
        print("ID da Nota fiscal:", self.id_nota)
        print("ID do Paciente:", self.id_paciente)
        print("Valor: R$", self.valor)
        print("Data de Emissão:", self.data_emissao)
        print("============================")
