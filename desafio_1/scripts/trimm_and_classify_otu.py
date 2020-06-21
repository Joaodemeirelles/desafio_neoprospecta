# Script para gera OTU table de dados de MiSeq 16s
# Eh necessario que script esteja na pasta "Desafio_Neoprospecta"

# Usagem: python trimm_and_classify_otu.py
# Output: Otu table


# Importando bibliotecas
from qiime2 import Artifact
from qiime2.plugins.dada2.methods import denoise_single
from qiime2.plugins.vsearch.methods import cluster_features_closed_reference
from qiime2.plugins.feature_classifier.methods import classify_sklearn
import sys
import subprocess
import os



########### Definicoes de funcoes ###########

def run_terminal(string): 
    '''Rodar o comando especificado na string no terminal'''
    returned_value = subprocess.call(string, shell=True)

def trimmar_dado(diretorio):
    ''' Funcao que trimma dados de NGS pelo Trim Galore com qualidade PHRED de 25
    e gera relatorio em html e txt
    Input: Caminho completo dos dados fastq 
    Output: Novo diretorio criado com todos arquivos trimmados'''

    temNGS = False                             # Variavel para salvar se ha algum NGS no diretorio
                                               # Se nao, no resultados devolver um erro que nao ha NGS no diretorio

    os.chdir(diretorio)                      

    arquivos_fq = os.listdir(diretorio)      
    for arquivo in arquivos_fq:
        if ".fastq" in arquivo:
            temNGS = True                      # Se existe um arquivo NGS, diretorio esta correto


    if temNGS != True:                         # Devolve o erro de que diretorio passado nao possui arquivos necessarios

        raise Exception('O diretorio {} nao contem arquivos fq.gz trimmados pelo trim_galore\n'.format(diretorio))
               

    # QC antes de Trimm
    reports_before_trimm()


    # Trimm e QC apos Trimm
    trimm_and_report()


    for fq in os.listdir(os.getcwd()):

        if "trimmed" in fq:

            file_name = fq.split("_")[:5]
            separator = "_"
            file_name = separator.join(file_name)

            run_terminal("mv {} {}.fastq.gz".format(fq, file_name))


    run_terminal("cd .. && mkdir fqs_gz && cd {}".format(diretorio))

    run_terminal("mv *.fastq.gz ../fqs_gz && cd ..")





def reports_before_trimm():
    ''' Gera pasta com reports de QC de reads anterior a trimm '''

    os.mkdir("reports_before")

    fastqc_before_trimm = "fastqc *.fastq"

    run_terminal(fastqc_before_trimm)

    run_terminal("mv *.zip reports_before")

    run_terminal("mv *_fastqc.html reports_before")    


    fastqc_reports = os.listdir("reports_before")
    os.chdir("reports_before")

    # Agora, separar por sample os reports

    for file in fastqc_reports:

        sample = file.split("_")[0]

        print(sample)
        run_terminal("mkdir {}".format(sample))
        run_terminal("mv {} {}".format(file,sample))


    os.chdir("../")

def trimm_and_report():
    ''' Gera pasta com reports de QC de reads apos o Trimm '''

    os.mkdir("reports_after") 

    trim_galore = "/TrimGalore-0.6.5/trim_galore --quality 25 --max_length 250 --phred33 --fastqc *.fastq --gzip"   

    run_terminal(trim_galore)        

    run_terminal("mv *_fastqc.html reports_after")    

    run_terminal("mv *.txt reports_after")    

    run_terminal("mv *.zip reports_after")    



    fastqc_reports = os.listdir("reports_after")
    os.chdir("reports_after")

    # Agora, separar por sample os reports

    for file in fastqc_reports:

        sample = file.split("_")[0]

        print(sample)
        run_terminal("mkdir {}".format(sample))
        run_terminal("mv {} {}".format(file,sample))


    os.chdir("../")


###################################### Script com suas chamadas do API do QIIME 2 e trim_galore



###### Trim Galore trimming por qualidade PHRED, trimming de 25

working_directory = os.getcwd()

trimmar_dado(working_directory + "/fqs")


# Cria diretorio de resultados
os.chdir("../")
mkdir = "mkdir resultados"
run_terminal(mkdir)

########### Comandos que serao rodados no QIIME 2, baseado em Artifact API (https://docs.qiime2.org/2020.2/interfaces/artifact-api/)
########### e plugins methods (https://docs.qiime2.org/2020.2/plugins/)

# Importar dados ja demultiplexados
demux_seqs = Artifact.import_data('SampleData[SequencesWithQuality]',    working_directory + "/fqs_gz" , view_type="CasavaOneEightSingleLanePerSampleDirFmt")

# Importar banco de dados de seqs taxonomicas greengenes e classificador
database_fasta = Artifact.import_data('FeatureData[Sequence]', "99_otus_gg_13_8.fasta") 
taxonomy = Artifact.import_data('FeatureData[Taxonomy]',"99_otu_taxonomy_gg_13_8.txt",view_type='HeaderlessTSVTaxonomyFormat') 
classifier_gg = Artifact.load("gg-13-8-99-515-806-nb-classifier.qza")


# Dereplicar sequencias e filtro de chimeras, para posterior assinalacao em OTUs
table_seqs, seqs, stats = denoise_single(demultiplexed_seqs = demux_seqs, trunc_len = 250, chimera_method = "consensus", n_threads = 0)


# Gerar otus por meio de vsearch e classifier treinado em gg_99%
otu_table, cluster_seqs, unmatchseqs = cluster_features_closed_reference(sequences=seqs,table=table_seqs,reference_sequences=database_fasta,perc_identity=0.99,threads=4)
results_tax = classify_sklearn(reads = cluster_seqs, classifier = classifier_gg, n_jobs = -1)


# Salva arquivos importantes
Artifact.save(otu_table,filepath='{}/resultados/otu_table.qza'.format(working_directory))
Artifact.save(cluster_seqs,filepath='{}/resultados/seqs.qza'.format(working_directory))
Artifact.save(taxonomy,filepath='{}/resultados/taxonomy.qza'.format(working_directory))
Artifact.save(results_tax.classification,filepath='{}/resultados/results.qza'.format(working_directory))


# Cria OTU table
os.chdir("resultados")
run_terminal("qiime taxa collapse --i-table otu_table.qza --i-taxonomy results.qza --p-level 7 --o-collapsed-table resultado_resultados.qza")
run_terminal("qiime tools export --input-path resultado_resultados.qza --output-path .")
run_terminal("biom convert -i feature-table.biom -o otu_table.tsv --to-tsv")
run_terminal("sed -i '1d' otu_table.tsv")
run_terminal("sed -e s/#//g -i otu_table.tsv")
