# Importar biblioteca de comandos do sistema operacional
import os

# Importar biblioteca de gerenciamento de arquivos
import shutil

# Criar pasta com nome 'newdir'
os.mkdir("newdir")

# Criar arquivo com o nome 'newdoc' na pasta newdir com a função escrita 'w' e apelida-lo de 'documento'
with open('newdir/newdoc.txt','w') as documento:
    # Colocar o conteudo do documento dentro de uma variavel chamada 'conteudo'
    conteudo = documento.write("Conteudo do arquivo")

# Criar uma copia da pasta 'newdir' com o nome 'olddir'
shutil.copytree ('newdir', 'olddir')

#renomear o arquivo que esta dentro do 'olddir' para 'olddoc'
os.rename('olddir/newdoc.txt','olddir/olddoc.txt')

# Apresentar informação do arquivos na pasta 'olddir' na tela ocmo validação 
# Apelidar o caminho do 'olddir' como entrada
with os.scandir('olddir') as entrada:
        # Para cada conteudo com o apelidado de 'documento' existente no apelidado como 'entrada'
        for documento in entrada:
              #criar uma apresentação de texto como cada arquivo scaneado
              if documento.is_file():
                    print(f'Arquivos que foram deletados: {documento.name}')

# Deletar a pasta com os arquivos antigos
shutil.rmtree('C:/Users/Aluno/Desktop/Aluno/olddir')