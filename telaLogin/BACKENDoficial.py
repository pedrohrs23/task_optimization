import os
import time

with open('arquivo.txt', 'r') as f:
    conteudo = f.read()

# Substituindo a palavra desejada
conteudo = conteudo.replace('</nfeProc>','\n')

# Substituindo a palavra desejada
conteudo = conteudo.replace(';Paciente: ','	')
conteudo = conteudo.replace(';Data cirurgia: ','	')
conteudo = conteudo.replace(';Medico..: ','	')
conteudo = conteudo.replace(';Pl.saude: ','	')
conteudo = conteudo.replace('o><vNF>','	')
conteudo = conteudo.replace('</vNF></I','	')
conteudo = conteudo.replace('serie><nNF>','	')
conteudo = conteudo.replace('</nNF><dhEmi>','	')
conteudo = conteudo.replace('</dhEmi><tpNF>1</tpNF>','	')
conteudo = conteudo.replace('.',',')

with open('arquivo_atualizado.txt', 'w') as f: # Conteúdo gerado como um novo arquivo atualizado #
     f.write(conteudo)
    
time.sleep(2)

filename = "arquivo_atualizado.txt" # Exclusão

if os.path.exists(filename): # Verifica se o arquivo existe
    os.remove(filename)    # Exclui o arquivo
    print(f"Arquivo {filename} Excluído com sucesso.")
else:
    print(f"Arquivo {filename} Não encontrado.")