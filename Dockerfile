# Dockerfile para rodar Desafio 1 de classificacao de OTUs da Neoprospecta
FROM ubuntu:18.04

# Necessario para instalar trim_galore
RUN apt-get update && apt-get install -y curl && apt-get install -y fastqc && apt-get install -y cutadapt && apt-get install -y python3-pip
RUN python3 -m pip install --user --upgrade cutadapt
RUN curl -fsSL https://github.com/FelixKrueger/TrimGalore/archive/0.6.5.tar.gz -o trim_galore.tar.gz
RUN tar xvzf trim_galore.tar.gz

# Instalacao de Miniconda para Qiime2
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda


# Copiar os arquivos necessarios para conda, script e desafio
COPY qiime2-2020.2-py36-linux-conda.yml .
COPY trimm_and_classify_otu.py .
COPY Desafio_Neoprospecta.tar.xz .
COPY gg-13-8-99-515-806-nb-classifier.qza .
COPY 99_otus_gg_13_8.fasta .
COPY 99_otu_taxonomy_gg_13_8.txt .


RUN conda env create -n qiime2-2020.2 --file qiime2-2020.2-py36-linux-conda.yml

#SHELL ["conda", "run", "-n", "qiime2-2020.2", "/bin/bash", "-c"]

#ENTRYPOINT ["conda", "run", "-n", "qiime2-2020.2"]

RUN tar -xf Desafio_Neoprospecta.tar.xz 

RUN mv trimm_and_classify_otu.py gg-13-8-99-515-806-nb-classifier.qza 99_otus_gg_13_8.fasta 99_otu_taxonomy_gg_13_8.txt Desafio_Neoprospecta 

RUN python3 -m pip install --user --upgrade cutadapt

RUN cd Desafio_Neoprospecta 

