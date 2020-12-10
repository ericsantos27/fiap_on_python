name = input("Nome do paciente: ")
age = int(input("Idade: "))
infectDisease = input("Suspeita de doença infectocontagiosa: ").upper()
if age > 65:
    print("Atendimento preferencial")
    if infectDisease == "SIM":
        print("Encaminhar paciente para sala de atendimento 'AMARELA'")
    elif infectDisease == "NAO":
        print("Encaminhar paciente para sala de atendimento 'BRANCA'")
    else:
        print("Responda sobre doença infectocontagiosa com SIM ou NAO")
else:
    print("Atendimento sem prioridade")
    if infectDisease == "SIM":
        print("Encaminhar paciente para sala de atendimento 'AMARELA'")
    elif infectDisease == "NAO":
        print("Encaminhar paciente para sala de atendimento 'BRANCA'")
    else:
        print("Responda sobre doença infectocontagiosa com SIM ou NAO")
