# Resultado de Desafio parte 1 da Neoprospecta

<p>
Para rodar o Docker, os comandos sao:

**docker pull jlmeirelles/desafio_neoprospecta_1:latest**

**sudo docker run -it --entrypoint /bin/bash**

**conda run -n qiime2-2020.2 python trimm_and_classify_otu.py** <br />
</p>

<p>
Dentro da pasta "fqs", estaram as pastas "reports_after" e "reports_before", referentes aos desafios 1.1 e 1.2

Dentro da pasta "resultados", o arquivo "otu_table.tsv" eh a resposta do ponto 1.4

O script "trimm_and_classify_otu.py" esta na pasta "scripts" desse repositorio, referente ao desafio 1.5.

O Dockerfile esta na pasta "scripts" desse repositorio, respondendo o desafio 1.6.
</p>

<p>
Apos os comandos rodados, para analisar os arquivos fora do container, o comando:

**sudo docker export jlmeirelles/desafio_neoprospecta_1 > container.tar**
</p>
