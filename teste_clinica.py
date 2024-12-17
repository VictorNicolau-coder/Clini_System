from classes.paciente import paciente
from classes.medico import medico
from classes.consulta import consulta
from classes.notafiscal import notafiscal

paciente1 = paciente(1, "Amanda Lira", 29, "88999999999", "Rua Alta, 55")
paciente2 = paciente(2, "Graziella Mendes", 18, "88988888888", "Av. Brasil, 123")
medico1 = medico(1, "Dra. Fernanda Costa", "Nutricionista", "12345-CE", "88 3456-5647")
medico2 = medico(2, "Dr. João Silva", "Cardiologista", "67890-CE", "88 3455-2100")
consulta1 = consulta(1, 1, 1, "16/12/2024", "08:00")
consulta2 = consulta(2, 2, 2, "16/12/2024", "10:00")
nota1 = notafiscal(1, 1, 300.00, "16/12/2024")
nota2 = notafiscal(2, 2, 300.00, "17/12/2024")

print("Ficha dos pacientes:")
paciente1.imprime_ficha()
paciente2.imprime_ficha()

print("Ficha dos médicos:")
medico1.imprime_ficha()
medico2.imprime_ficha()

print("Consultas")
consulta1.imprime_consulta()
consulta2.imprime_consulta()

print("Notas Fiscais")
nota1.emitir()
nota2.emitir()