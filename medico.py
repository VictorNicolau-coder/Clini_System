class medico:
    def __init__(self, id_medico, nome, especialidade, crm, telefone):
        self.id_medico = id_medico
        self.nome = nome
        self.especialidade = especialidade
        self.crm = crm  # Registro do médico
        self.telefone = telefone

    #Nome de função substituído para não causar erro no entendimento
    def imprime_consulta(self):
        print("============================")
        print("ID do Médico:", self.id_medico)
        print("Nome:", self.nome)
        print("Especialidade:", self.especialidade)
        print("CRM:", self.crm)
        print("Telefone:", self.telefone)
        print("============================")
