# Dados
name = input("Nome: ")
age = int(input("Idade: "))
infectDes = input("Possui doença infectocontagiosa? 'SIM' ou 'NAO': ").upper()

# Primeiro problema
if infectDes == 'SIM':
    print("Encaminhe o paciente para a ala 'AMARELA'")
elif infectDes == 'NAO':
    print("Encaminhe o paciente para a ala 'BRANCA'")
else:
    print("Informe 'SIM' ou 'NAO' para doença infectocontagiosa")

# Segundo problema
if age >= 65:
    print("Atendimento PRIORITÁRIO")
else:
    genre = input("Informe o gênero do paciente: ").upper()
    if genre == "FEMININO" and age > 10:
        pregnancy = input("A paciente é gestante: ")
        if pregnancy == "SIM":
            print("Atendimento PRIORITÁRIO")
        else:
            print("Atendimento NÃO PRIORITÁRIO")
    else:
        print("Atendimento NÃO PRIORITÁRIO")
