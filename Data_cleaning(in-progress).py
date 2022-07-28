# Importing necessary libraries:
import os
import pandas as pd
import re
import numpy as np

# Loading all files from the Group:
folder = r'C:/Users/Harini01.R/Desktop/Git/Microbiome-project/import_data/GroupA'
files = os.listdir(folder)
pwyfiles = []
ecsfiles = []
genfiles = []
taxfiles = []

for file in files:
    if re.search(r"path", file):
        pwyfiles.append(f"{folder}/{file}")
    elif re.search(r"ecs", file):
        ecsfiles.append(f"{folder}/{file}")
    elif re.search(r"gene", file):
        genfiles.append(f"{folder}/{file}")
    elif re.search(r"taxon", file):
        taxfiles.append(f"{folder}/{file}")
        
# Pre-processing the individual files:
visitname = []
for file in pwyfiles:
    visitname.append(file[70:78])
    
def pwypreprocess_1(df):
    otu = df.OTU_ID
    otup = otu.str.split(':')
    df["PWY"] = ""
    for i in range (0,len(otup)):
        df.PWY[i] = otup[i][0]
    otug = otu.str.split('|')
    df["Genus"] = ""
    for j in range(0,len(otug)):
        if(len(otug[j])<=1):
            df.Genus[j] = 0
        else:
            df.Genus[j] = otug[j][1]
    return df

def pwypreprocess_2(df):
    df = df.drop(df[df['Genus'] == 0].index)
    df = df.drop(df[df['Genus'] == 'unclassified'].index)
    df = df.drop(df[df['Abundance'] == 0].index)
    df = df.drop('OTU_ID', axis = 1)
    if 'taxonomy' in df.columns:
        df = df.drop('taxonomy', axis = 1)
    return df

for i in range(0, len(pwyfiles)):
    df = pd.read_table(pwyfiles[i])
    df_1 = pwypreprocess_1(df)
    df_2 = pwypreprocess_2(df_1)
    df_2["Visit_name"] = visitname[i]
    #print(df_2)
    pwyfiles[i] = df_2

# Merging the files & downloading the merged file(s):
    
for i in range(0, len(pwyfiles)):
    GroupApwyfiles = pd.concat(pwyfiles)
    
GroupApwyfiles.to_csv('Pathways_GroupA_processed.csv')
