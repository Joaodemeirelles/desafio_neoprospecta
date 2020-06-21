# Resultado de Desafio parte 1 da Neoprospecta

Link do Docker: https://hub.docker.com/repository/docker/jlmeirelles/desafio_neoprospecta_1
<p>
Para rodar o Docker, os comandos sao:

**docker pull jlmeirelles/desafio_neoprospecta_1:latest**

**docker run --name desafio -it --entrypoint /bin/bash jlmeirelles/desafio_neoprospecta_1**

**cd Desafio_Neoprospecta**

**conda run -n qiime2-2020.2 python trimm_and_classify_otu.py**
</p>

<p>&nbsp;</p>

<p>
Apos os comandos rodados, para analisar os arquivos fora do container:

**<abrir outro terminal com o container aberto e rodar:>**

**docker cp desafio:/Desafio_Neoprospecta/ .**

Dentro da pasta "fqs", estarao as pastas "reports_after" e "reports_before", referentes aos desafios 1.1 e 1.2

Dentro da pasta "resultados", o arquivo "otu_table.tsv" eh a resposta do ponto 1.4
</p>

<p>&nbsp;</p>

<p>
Neste Github, estao todos os arquivos de interesse citados anteriormente apos seguir o mesmo pipeline. 
  
Dentro da pasta "respostas" estao as pastas "reports_after" e "reports_before", referentes aos desafios 1.1 e 1.2

Dentro da pasta "scripts", esta o arquivo "trimm_and_classify_otu.py", responsavel pela resposta dos desafios 1.3, 1.4 e 1.5.

Na pasta "scripts", tambem esta o Dockerfile responsavel pela resposta ao desafio 1.6.
</p>

