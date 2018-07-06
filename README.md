# MRPSystem
This repository contains the implementation of a MRP system in the context of the course Modelagem da Produção - july 2018


## Executável (Windows)

Para executar o programa no Windows, baixe o executável "MRPSystem.exe" (dist/MRPSystem.exe) e o execute normalmente.

Link: https://github.com/gustavo-moura/MRPSystem/blob/master/dist/MRPSystem.exe
(Clique em "Download" e execute o programa)

Obs. Dentro do programa, vá até a aba "Arquivo -> Ajuda" para obter mais instruções sobre o uso.


## Especificações técnicas

REQUISITOS MÍNIMOS

Para rodar, é necessário instalar o PyQt5 (utilize o comando "pip install PyQt5") [não sei se funciona no Arch]


EXECUÇÃO

Para iniciar o programa, execute o arquivo "app.py"


ENTENDENDO O CÓDIGO

app.py: é responsável pela definição inicial e principal do aplicativo. Nele são declaradas as execuções dos botões da interface, a inicialização do sistema e as principais funções

main.ui: é o arquivo de construção de interface utilizado pelo Qt Designer (utilizado somente no desenvolvimento)

main.py: é o arquivo correspondente ao "main.ui", em python, declarando toda a interface e composição dos elementos

object.py: é um arquivo que une todas as classes de objetos utilizados no sistema, é um arquivo de apoio e organização
