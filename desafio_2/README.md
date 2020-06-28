# Resultado de Desafio parte 2 da Neoprospecta

Link do Docker: https://hub.docker.com/repository/docker/jlmeirelles/desafio_neoprospecta_1
<p>
Para rodar o Docker, os comandos sao:
  
**sudo docker run  --name desafio_2 -p 5100:5100 -it desafio2:latest bash**

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
Neste Github, estao todos os arquivos de interesse citados anteriormente apos seguir o mesmo pipeline. 
  
Dentro da pasta "respostas" estao as pastas "reports_after" e "reports_before", referentes aos desafios 1.1 e 1.2

Dentro da pasta "scripts", esta o arquivo "trimm_and_classify_otu.py", responsavel pela resposta dos desafios 1.3, 1.4 e 1.5.

Na pasta "scripts", tambem esta o Dockerfile responsavel pela resposta ao desafio 1.6.
</p>

