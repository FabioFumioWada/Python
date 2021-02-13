import requests

#Faz requisição ao webservice no formato json

#https://viacep.com.br/

#Solicita o CEP para consulta
print('-----------------------------')
print('         CONSULTA CEP        ')
print('                             ')
print('        WebService\Json      ')
print('-----------------------------')

v_cep_input = input('--> Digite o CEP para consulta: ')

#verifica se o CEP informado possuí 8 dígitos
if len(v_cep_input) != 8:
    print('--> Quantidade de dígitos inválido! <--')
    exit()
   
#Faz a requisição para o webservice no formato json
v_requisicao_cep = requests.get('https://viacep.com.br/ws/{}/json/'.format(v_cep_input))

#Armazena os dados recebidos da requisição ao webservice
v_dados_requisicao = v_requisicao_cep.json()

#Não existindo a palavra "erro" nos dados recebidos do webservice, a condição "if" é realizada
if 'erro' not in v_dados_requisicao:
    print()
    print('--> CEP Encontrado <--')
    print()
    print('--> Dados recebidos (json) <--')
    print(v_dados_requisicao)
    print()
    print('--> Dados recebidos (json/formatado) <--')
    print('    CEP: {}'.format(v_dados_requisicao['cep']))
    print('    ENDEREÇO: {}'.format(v_dados_requisicao['logradouro']))
    print('    COMPLEMENTO: {}'.format(v_dados_requisicao['complemento']))
    print('    BAIRRO: {}'.format(v_dados_requisicao['bairro']))
    print('    CIDADE: {}'.format(v_dados_requisicao['localidade']))
    print('    UF: {}'.format(v_dados_requisicao['uf']))
    print()
    print()
else:
    print('--> O CEP {} é inválido e/ou a consulta não foi realizada com sucesso <--'.format(v_cep_input))
    print()


#print(v_dados_requisicao)