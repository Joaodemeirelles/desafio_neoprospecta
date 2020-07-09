# Resultado de Desafio parte 2 da Neoprospecta

Link do Docker: https://hub.docker.com/repository/docker/jlmeirelles/desafio_neoprospecta_2
<p>
Para rodar o Docker, os comandos são:
 
1. Pull do Docker Hub:
```
docker pull jlmeirelles/desafio_neoprospecta_2:latest
```

2. Criar container de imagem:

```
docker run --name desafio_2 jlmeirelles/desafio_neoprospecta_2
```

</p>

<p>
4. Após os comandos rodados, para analisar os arquivos fora do container:
 
```
docker cp desafio_2:/meus_dados/ .

docker cp desafio_2:/dados_recebidos/ .

```

</p>

<p>&nbsp;</p>

<p>
  
Dentro do diretório "resultados" estão os diretórios "meus_dados", aonde os pontos 2.1, 2.2 e 2.3 foram executados na OTU table gerada pelo pipeline seguido na minha resposta da parte 1 e "dados_recebidos", aonde foram executadas na OTU table dada como resposta na pasta "tables".

Nos diretórios "meus_dados" e "dados_recebidos", os arquivos: 

"Otu_Table_plot_absolute.png" e "Otu_Table_plot_percent.png" respondem o ponto 2.1.

"PCoA_plot.png" responde o ponto 2.2.

"desmame_tarde_vs_cedo.csv" responde o ponto 2.3.
</p>

<p>&nbsp;</p>

<p>
Dentro do diretório "scripts", estão os scripts utilizados nessa etapa do desafio:

O arquivo "Dockerfile" que roda todas as analises e os scripts em R utilizados para análise estatística e visual.

O script "otu_plot.txt" responde ao ponto 2.1.

O script "pcoa_plot.txt" responde ao ponto 2.2.

O script "deseq2_otu.txt" responde ao ponto 3.3.
</p>

