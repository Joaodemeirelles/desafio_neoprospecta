# Script para formatar a OTU table em um dataframe com as 50 OTUs mais abundantes
# Usagem: python format_otu_table.py nome_arquivo.tsv nome_output.tsv
# Exemplo: python format_otu_table.py otu_table_tax_amostras.tsv new_otu_table.tsv


import sys

# Dictionario aonde OTU's mais abundantes vao ser salvas
# Chave = Nome de OTU, Valor = Contagem de OTU em todas as samples
dict_OTUs = {}


file_name = sys.argv[1]
formated_output_file_name = sys.argv[2]


with open(file_name,"r") as old:
    with open(formated_output_file_name,"w") as new:
        

        all_data = [] # Lista que contem todos os dados


        for line in old:

            if "OTU" in line:

                header = line.split("\t") # Salva o Header
                header[-1] = header[-1].replace("\n","")


            else:                   # Se linha nao tem "OTU", eh dados

                data = line.split()
                try:    # Erros de formatacao
                    float(data[1])

                except:
 
                    data[1] = data[0] + data[1]
                    data = data[1:]


                all_data.append(data)

        for item in all_data:

            flag = False
            OTU = ";".join(item[0].split(";")[3:])

            for i in range(1,len(item)-1):    # Para cada coluna do antigo tsv, tirando header


                count = item[i]               

                if OTU not in dict_OTUs.keys():
                    dict_OTUs[OTU] = int(float(count))

                else:

                    dict_OTUs[OTU] = dict_OTUs[OTU] + int(float(count))


        list_OTUs = []                                  # Lista de todos OTUs

        for key in dict_OTUs.keys():
            list_OTUs.append([key,dict_OTUs[key]])

        list_OTUs.sort(key = lambda x: x[1],reverse=True)  # Descrescente por contagem de OTU
        list_OTUs = list_OTUs[0:50]                        # Pega 50 mais abundantes
        temp = []
        temp.extend(OTU[0] for OTU in list_OTUs) 
        list_OTUs = temp


        # Gera tsv em ordem para utilizacao em analises estatisticas no R

        new.write("OTU\tDesmame\tContagem\n")    
        for item in all_data:


            OTU = ";".join(item[0].split(";")[3:])
            for i in range(1,len(item)-1):   


                count = item[i] 

                try:
                    sample_type = str(int(header[i].replace("F3D","")[0:3]))


                except:

                    sample_type = str(int(header[i].replace("F3D","")[0]))

                if OTU in list_OTUs:
                    new.write("{}\t{}\t{}\n".format(OTU,sample_type,count))












