# Script para remover duplicatas de OTU table

import sys


file_name = sys.argv[1]
new_file_name = sys.argv[2]

dict_OTUs = {}


with open(file_name,"r") as old:
    with open(new_file_name,"w") as new:



        all_data = [] # Lista que contem todos os dados


        for line in old:

            if "OTU" in line:

                header = line


            else:                   # Se nao existe 'OTU' na linha, a linha eh dado

                data = line.split() # Take data

                data[1] = data[1] + "_" + data[2] 
                data.pop(0)
                all_data.append(data)


        for i in range(0,len(all_data)):

            OTU = "".join(all_data[i][0:1])

            if OTU not in dict_OTUs.keys():

                dict_OTUs[OTU] = all_data[i][2:]

            else:

                lista_juntos = zip(dict_OTUs[OTU],all_data[i][2:])

                dict_OTUs[OTU] = [int(x) + int(y) for (x, y) in lista_juntos]

        new.write(header)
        for OTU in dict_OTUs.keys():

            count_string = ""
            for count in dict_OTUs[OTU]:

                count_string = count_string + "\t" + str(count) 


            new.write("{}{}\n".format(OTU,count_string))
    