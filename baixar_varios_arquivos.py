#Baixar vários arquivos na internet

#pip install requests

import requests

def fn_baixa_arquivo(url, endereco):
    #faz requisição no servidor
    resposta = requests.get(url)
    with open(endereco,'wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)

if __name__ == "__main__":
    fn_baixa_arquivo('https://nic.br/media/docs/publicacoes/2/20201123084414/tic_saude_2019_livro_eletronico.pdf','c:/users/fabio/teste.pdf')