### Protein Plus Run
### Using Protein Plus poseview API (ZBH - Center for Bioinformatics)
### JeongSoo Na
### Create At 2024.03.11
### Update At 2024.06.25

import os
import argparse

### Parameters
parser = argparse.ArgumentParser(description='Protein Ligand Interaction 2D Diagram')
parser.add_argument('--age', type=int, default=20, help='작성작의 나이를 입력하세요')
parser.add_argument('--name', type=str, default='홍길동')



### Process
### Create PDB code in API -> Images Generation -> Get Images
### LIG_chain_num : If this ligand text is different from each pdb, please check algorithm and update.


### input pdb directory
pdb_dir = "/workspace/pdb"
pdb_list = os.listdir(pdb_dir)
#print(pdb_list)

### Run Protein Plus Command
### curl -F pdb_file[pathvar]=@/workspace/pdb/test.pdb -X POST https://proteins.plus/api/pdb_files_rest -H "Accept: application/json"
### curl -d '{"poseview": {"pdbCode":"testpdb66c21457-4969-4348-a00b-e04804d78fea","ligand":"LIG_A_298"}}' -H "Accept: application/json" -H "Content-Type: application/json" -X POST https://proteins.plus/api/poseview_rest

### Job
for i in pdb_list:

        ### 1. Create PoseView Job
        print("################################" + i)

        os.system("curl -F pdb_file[pathvar]=@" + pdb_dir + i + " -X POST https://proteins.plus/api/pdb_files_rest -H 'Accept: application/json' > temp")

        ### output : {"status_code":"accepted","location":"https://proteins.plus/api/pdb_files_rest/pdb_code","message":"Inspect PDB loading status in the specified location"}

        tmp_1 = open("temp","r")
        file_text = tmp_1.read()
        tmp_1.close()

        pdb_code = file_text.split("pdb_files_rest/")[1].split('","message"')[0]
        #print(pdb_code)



        ### 2. Show PoseView Job

        os.system('''curl -d '{"poseview": {"pdbCode":"''' + pdb_code + '''","ligand":"UNK__0"}}' -H "Accept: application/json" -H "Content-Type: application/json" -X POST https://proteins.plus/api/poseview_rest > temp''')

        tmp_2 = open("temp","r")
        file_text = tmp_2.read()
        #print("specified location : " + file_text)
        #specified location : {"status_code":202,"location":"https://proteins.plus/api/poseview_rest/U2DE7VwFUgUF5ueYXYu2K4bY","message":"The job will be created in the specified location"}
        final_code = file_text.split('poseview_rest/')[1].split('","')[0]
        #print(final_code)
        tmp_2.close()



        ### 3. Get Images
        os.system("wget https://proteins.plus/results/poseview/" + final_code + "/" + pdb_code + "_UNK__0.png")
        os.system("cp " + pdb_code + "_UNK__0.png " + "kras_2d/"+ i.replace(".pdb",".png"))
        os.remove(pdb_code + "_UNK__0.png")
