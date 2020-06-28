FROM bioconductor/bioconductor_docker:devel

# Instala pacotes necessarios
RUN R -e 'BiocManager::install("DESeq2")' \
	R -e 'install.packages("ggplot2")' \
	R -e 'install.packages("RColorBrewer")' \
	R -e 'install.packages("vegan")'


# Copia OTU tables e scripts para formatacao

COPY otu_table.tsv . 
COPY otu_table_tax_amostras.tsv . 
COPY format_otu_table.py .
COPY format_otu_table_dado.py .
