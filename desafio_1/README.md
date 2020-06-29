# Resultado de Desafio parte 1 da Neoprospecta

Link do Docker: https://hub.docker.com/repository/docker/jlmeirelles/desafio_neoprospecta_1

<p>
Para rodar o Docker, os comandos são:

**docker pull jlmeirelles/desafio_neoprospecta_1:latest**

**docker run --name desafio_1 -it --entrypoint /bin/bash jlmeirelles/desafio_neoprospecta_1**

**cd Desafio_Neoprospecta**

**conda run -n qiime2-2020.2 python trimm_and_classify_otu.py**
</p>

<p>&nbsp;</p>

<p>
Após os comandos rodados, para analisar os arquivos fora do container:

**<abrir outro terminal com o container aberto e rodar:>**

**docker cp desafio_1:/Desafio_Neoprospecta/ .**

Dentro da pasta "fqs", estarão as pastas "reports_after" e "reports_before", referentes aos desafios 1.1 e 1.2 e o arquivo "otu_table.tsv", resposta do ponto 1.4

Dentro da pasta "resultados", o arquivo "otu_table.tsv" é a resposta do ponto 1.4
</p>

<p>&nbsp;</p>

<p>
Neste Github, estão todos os arquivos de interesse citados anteriormente apos seguir o mesmo pipeline. 
  
Dentro da pasta "respostas" estão as pastas "reports_after" e "reports_before", referentes aos desafios 1.1 e 1.2, e o arquivo "otu_table.tsv", referente ao desafio 1.4

Dentro da pasta "scripts", está o arquivo "trimm_and_classify_otu.py", responsável pela resposta dos desafios 1.3, 1.4 e 1.5.

Na pasta "scripts" está o Dockerfile responsável pela resposta ao desafio 1.6.
</p>

