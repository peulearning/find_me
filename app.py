import requests

def main():

  print('=============================')
  print(' ==== Search by Postal Codes ==== ')
  print('=============================')
  print()

cep_input = input ('Enter Postal Code For Consultation :')

if len(cep_input) !=8:
   print('Number of invalid digits !!! ')
   exit()


request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

address_data = request.json()

if 'erro' not in address_data:
		print('==> CEP FOUND <==')

		print('CEP: {}'.format(address_data['cep']))
		print('Street: {}'.format(address_data['logradouro']))
		print('Complement: {}'.format(address_data['complemento']))
		print('Neighborhood: {}'.format(address_data['bairro']))
		print('City: {}'.format(address_data['localidade']))
		print('State: {}'.format(address_data['uf']))

else:
		print('{}: CEP INVALID.'.format(cep_input))

print('---------------------------------')
option = int(input('Do you want make a new query ?\n1. YES \n2. EXIT\n'))
if option == 1:
          main()
else:
		print('Ty for using the code EXITING ...')


if __name__ == '__main__':
	main()