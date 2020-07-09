# Resultado de Desafio parte 1 da Neoprospecta

Link do Docker: https://hub.docker.com/repository/docker/jlmeirelles/desafio_neoprospecta_1

<p>
Para rodar o Docker, os comandos são: 

1. Pull do Docker do Docker Hub
 ```
docker pull jlmeirelles/desafio_neoprospecta_1:latest
 ```
 
2. Criar container iterativo de imagem

 ```
docker run --name desafio_1 -it --entrypoint /bin/bash jlmeirelles/desafio_neoprospecta_1
 ```
 
3. Dentro do container, rodar script

 ```
conda run -n qiime2-2020.2 python trimm_and_classify_otu.py
 ```

4. Copiar o diretório para fora do container:

 ```
docker cp desafio_1:/Desafio_Neoprospecta/ .

 ```
 </p>
 <p>&nbsp;</p>
 
<p>
  
Dentro do diretório "fqs":
- Os diretórios "reports_after" e "reports_before", referentes aos desafios 1.1 e 1.2 

- O arquivo "otu_table.tsv", resposta do ponto 1.4


Dentro da pasta "resultados", o arquivo:

- "otu_table.tsv" é a resposta do ponto 1.4
</p>

<p>&nbsp;</p>

<p>
Neste Github, estão todos os arquivos de interesse citados anteriormente após seguir o mesmo pipeline. 
  
Dentro do diretório "respostas":
- Diretórios "reports_after" e "reports_before", referentes aos desafios 1.1 e 1.2

- O arquivo "otu_table.tsv", referente ao desafio 1.4

Dentro da pasta "scripts", o arquivo:

- "trimm_and_classify_otu.py", responsável pela resposta dos desafios 1.3, 1.4 e 1.5.

- "Dockerfile" responsável pela resposta ao desafio 1.6.
</p>

