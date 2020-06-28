FROM bioconductor/bioconductor_docker:devel

# Instala pacotes necessarios
RUN R -e 'BiocManager::install("DESeq2")' \
	R -e 'install.packages("ggplot2")' \
	R -e 'install.packages("RColorBrewer")' \
	R -e 'install.packages("vegan")' \
	R -e 'BiocManager::install("apeglm")'


# Copia OTU tables e scripts para formatacao

COPY otu_table.tsv .
COPY otu_table_tax_amostras.tsv . 
COPY format_otu_table.py .
COPY format_otu_table_dado.py .
COPY pcoa_plot.txt .
COPY otu_plot.txt .
COPY deseq2_otu.txt .
COPY metadata.csv .


# Roda scripts nos meus dados
RUN mkdir meus_dados
RUN cp *.csv *.txt *.py otu_table.tsv meus_dados
RUN cd meus_dados && \
	Rscript pcoa_plot.txt otu_table.tsv && \
	python format_otu_table.py otu_table.tsv meus_dados.tsv && \
	Rscript otu_plot.txt meus_dados.tsv && \
	Rscript deseq2_otu.txt otu_table.tsv

# Roda scripts em dados recebidos como resposta

RUN cd / && mkdir dados_recebidos
RUN mv *.csv *.txt *.py otu_table_tax_amostras.tsv dados_recebidos
RUN cd dados_recebidos && \
	Rscript pcoa_plot.txt otu_table_tax_amostras.tsv && \
	python format_otu_table_dado.py otu_table_tax_amostras.tsv dados_recebidos.tsv && \
	Rscript otu_plot.txt dados_recebidos.tsv && \
	Rscript deseq2_otu.txt otu_table_tax_amostras.tsv
