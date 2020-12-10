pacient = input('Nome: ')
age = int(input('Idade: '))
infectDisease = input('Doença infectuosa: ')
if age >= 65 and infectDisease == 'SIM':
	print('Atendimento preferencial na sala Amarela')
elif age < 65 and infectDisease == 'SIM':
	print('Atendimento não preferencial na sala Amarela')
elif age >= 65 and infectDisease == 'NÃO':
	print('Atendimento preferencial na sala Branca')
elif age < 65 and infectDisease == 'NÃO':
	print('Atendimento não preferencial na sala Branca')
else:
	print('Informe doença infectuosa com "SIM" ou "NÃO"')

