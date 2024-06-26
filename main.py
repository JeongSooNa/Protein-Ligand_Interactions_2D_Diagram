import os
import argparse
import time

def get_pdb_code(pdb):
        ### Protein Plus API
        os.system("curl -F pdb_file[pathvar]=@" + pdb + " -X POST https://proteins.plus/api/pdb_files_rest -H 'Accept: application/json' > temp")
        tmp = open("temp","r")
        text = tmp.read()
        tmp.close()
        try:
                pdb_code = text.split("pdb_files_rest/")[1].split('","message"')[0]
        except:
                return ""
        
        return pdb_code

def get_file_code(pdb_code,lig_code):
        ### Protein Plus API
        os.system('''curl -d '{"poseview": {"pdbCode":"''' + pdb_code + '''","ligand":"''' + lig_code + '''"}}' -H "Accept: application/json" -H "Content-Type: application/json" -X POST https://proteins.plus/api/poseview_rest > temp''')
        
        tmp = open("temp","r")
        text = tmp.read()
        try:
                file_code = text.split('poseview_rest/')[1].split('","')[0]
        except:
                return ""
        
        return file_code

def get_png_file(pdb,pdb_code, file_code,lig_code,output_dir):
        img = pdb_code + "_" + lig_code + ".png"
        os.system("wget https://proteins.plus/results/poseview/" + file_code + "/" + img)
        os.system("cp " + img + " " + output_dir + "/" + pdb.replace(".pdb",".png"))
        os.remove(img)
        
        return 0

def main():
        print("#################################\n#####Protein-Plus 2D Diagram#####\n#################################")
        
        ### Set Arguments
        parser = argparse.ArgumentParser(description='Protein Ligand Interaction 2D Diagram')
        ### The input PDB path must be absolute path
        parser.add_argument('--pdb', type=str, default="test.pdb", help="Please enter pdb files path")
        ### Input Ligand code
        parser.add_argument('--lig', type=str, default="UNK__0", help="Please enter ligand Residue_Chain_Num")
        ### output directory
        parser.add_argument('--output_dir', type=str, default="/", help="Please enter output directory")
        
        config = parser.parse_args()
        
        ### Ligand Code : Residue_Chain_Num
        lig_code = config.lig
        
        ### PDB code in Protein-Plus REST API service
        pdb_code = get_pdb_code(config.pdb)
        if pdb_code == "":
                time.sleep(60)
                pdb_code = get_pdb_code(config.pdb)
                if pdb_code == "":
                        print("Error : Please Check pdb files or parameters")
                        exit()
                        
        ### File code in Protein-Plus REST API service
        file_code = get_file_code(pdb_code,lig_code)
        if file_code == "":
                time.sleep(60)
                pdb_code = get_file_code(pdb_code,lig_code)
                if file_code == "":
                        print("Error : Please Check pdb files or parameters")
                        exit()
                        
        ### Copy png file to output directory & remove png file
        get_png_file(config.pdb,pdb_code,file_code,lig_code,config.output_dir)
        
        print("Job Done")
        
if __name__== "__main__":
        main()