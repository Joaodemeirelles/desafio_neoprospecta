# Resultado de Desafio parte 2 da Neoprospecta

Link do Docker: https://hub.docker.com/repository/docker/jlmeirelles/desafio_neoprospecta_1
<p>
Para rodar o Docker, os comandos sao:
  
**docker pull jlmeirelles/desafio_neoprospecta_2:latest**
  
**docker run --name desafio_2 -it --entrypoint /bin/bash jlmeirelles/desafio_neoprospecta_2**

</p>

<p>&nbsp;</p>

<p>
Apos os comandos rodados, para analisar os arquivos fora do container:

**<abrir outro terminal com o container aberto e rodar:>**

**docker cp desafio_2:/meus_dados/ .**

**docker cp desafio_2:/dados_recebidos/ .**

</p>

<p>&nbsp;</p>

<p>
  
Dentro da pasta "respostas" estao a pasta "meus_dados", aonde os pontos 2.1, 2.2 e 2.3 foram executados na OTU table gerada pelo pipeline seguido na minha resposta da parte 1 e a pasta "dados_recebidos", aonde foram executadas na OTU table dada como resposta na pasta "tables".

Dentro da pasta "scripts", esta o Dockerfile que roda todas as analises e os scripts em R utilizados para analise estatistica e visual.

O script "otu_plot.txt" responde ao ponto 2.1.

O script "pcoa_plot.txt" responde ao ponto 2.2.

O script "deseq2_otu.txt" responde ao ponto 3.3.

Na pasta "scripts", tambem esta o Dockerfile responsavel pela resposta ao desafio 1.6.
</p>

