#!/usr/bin/env python3
import sys
import re
import biom
import requests
import os
import pandas as pd

excel_file = sys.argv[1]

# Function to download the file from url and save it locally
def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))
    return file_path

# Function to clean the column names
# It replaces <sample_name>_Abundance to Abundance to make it generic for loading when you have to reference the column name
def convert_group(match_obj):
    if match_obj.group(1) is not None:
        result = re.sub(".*_Abundance","Abundance",match_obj.group(1)) 
        return result

######### Python script #########
# 1. Downloads file by url and save it locally
# 2. Converts biom format to tsv (table separated values) format using biom-format Python package
# 3. Modifies tsv file to make it ready for neo4j loading
#################################

# Read file URLs from Excel 
df = pd.ExcelFile(excel_file).parse('Sheet1')

# Loop through urls
for url in df['urls'].values:
    try:
        print(url)
        # Check if the file already processed
        
        # Download file
        file_path = download(url, dest_folder=".\data")

        # Convert biom into tsv format
        biom_table = biom.load_table(file_path)
        tsv_filename = file_path.replace("data","import_data") + ".tsv"

        with open(tsv_filename, "w") as f:
            biom_table.to_tsv(header_key="taxonomy", header_value="taxonomy",direct_io=f)

        # Modify tsv file to prepare it for neo4j loading
        with open(tsv_filename, 'r') as fin:
            lines = fin.readlines()
            lines[1] = lines[1][1:].replace("OTU ID", "OTU_ID") #removes the first symbol of the second line (it's "#" that neo4j doesn't like)
            lines[1] = re.sub(r"(\w*\W)", convert_group, lines[1])
            lines[1] = lines[1].replace("-RPKs", "_RPKs")
            #new_lines = [re.sub('[k,f,s,q,g,p,c,o,t]__', '', s) for s in lines]
            new_lines = [re.sub('.s__', '|s__', s) for s in lines]
        with open(tsv_filename, 'w') as fout:
            fout.writelines(new_lines[1:]) # removes the first line before saving
    except:
        print("Something went wrong with the file: " + url)