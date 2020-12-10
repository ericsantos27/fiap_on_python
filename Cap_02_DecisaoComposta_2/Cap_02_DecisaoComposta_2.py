pacient = input('Nome: ')
age = int(input('Idade: '))
infectDisease = input('Doença infectuosa: ').upper()
if age >= 65:
	print('Atendimento preferencial')
elif infectDisease == 'SIM':
	print('Atendimento emergencial')
else:
	print('Atendimento comum')
