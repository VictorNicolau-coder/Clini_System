class consulta:
    def __init__(self, id_consulta, id_paciente, id_medico, data, horario):
        self.id_consulta = id_consulta
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.data = data
        self.horario = horario

    def imprime_consulta(self):
        print("============================")
        print("Consulta Agendada com Sucesso!")
        print("ID da Consulta:", self.id_consulta)
        print("ID do Paciente:", self.id_paciente)
        print("ID do Médico:", self.id_medico)
        print("Data:", self.data)
        print("Horário:", self.horario)
        print("============================")
