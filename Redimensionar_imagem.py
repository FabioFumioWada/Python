import os

#pip install Pillow
from PIL import Image

def fn_tipo_arquivo_imagem(nome_arquivo):
    if nome_arquivo.endswith('png'):
        return True
    return False



#função para reduzir as imagens
def fn_reduzir_tamanho_imagens(v_input_dir, v_output_dir):
    
    v_lista_de_arquivos = os.listdir(v_input_dir)
    
        #v_lista_de_arquivos[0] #pega a primeira imagem
    
    for v_nome_arquivo in v_lista_de_arquivos:

        #v_imagem = Image.open(os.path.join(v_input_dir, v_lista_de_arquivos[0])) #[0]--posição do arquivo
        v_imagem = Image.open(os.path.join(v_input_dir, v_nome_arquivo)) #[0]--posição do arquivo

        #resize(largura&comprimento , altura)
            #1280x720  -- HD
            #1980x1080 -- Full HD
        v_imagem_redimensionada = v_imagem.resize((1980,1080))
        
        #v_imagem_redimensionada.save(os.path.join(v_output_dir, v_lista_de_arquivos[0])) #[0]--posição do arquivo
        v_imagem_redimensionada.save(os.path.join(v_output_dir, v_nome_arquivo)) #[0]--posição do arquivo
    
    #mostra a imagem
    #imagem.show() 
    
    #print(v_lista_de_arquivos)

#principal
if __name__ == "__main__":
    #diretório origem da imagem
    v_diretorio = 'C:/Imagem'

    #execução da function e geração do novo arquivo redimensionado
    fn_reduzir_tamanho_imagens(v_diretorio, 'C:/Imagem/Output')
