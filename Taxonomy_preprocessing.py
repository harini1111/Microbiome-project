#!/usr/bin/env python
# coding: utf-8

# Step 1/4: Importing necessary libraries:

# In[ ]:


import os
import pandas as pd
import re
import numpy as np


# Step 2/4: Loading all files from the Group:

# In[ ]:


#Use folder where the files to be processed are placed 
folder = r'C:/Users/Harini01.R/Desktop/Git/Microbiome-project/import_data/UC'
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


# Step 3/4: Pre-processing the individual files:

# In[ ]:


visitname = []
for file in taxfiles:
    visitname.append(file[66:74])


# In[ ]:


def taxpreprocess_1(df):
    otu = df.OTU_ID
    otup = otu.str.split('|')
    df["Kingdom"] = ""
    df["Phylum"] = ""
    df["Class"] = ""
    df["Order"] = ""
    df["Family"] = ""
    df["Genus"] = ""
    df["Species"] = ""
    df["t__"] = ""
    for i in range(0,len(otup)):
        if len(otup[i]) == 1:
            df.Kingdom[i] = otup[i][0]
        if len(otup[i]) == 2:
            df.Kingdom[i] = otup[i][0]
            df.Phylum[i] = otup[i][1]
        if len(otup[i]) == 3:
            df.Kingdom[i] = otup[i][0]
            df.Phylum[i] = otup[i][1]
            df.Class[i] = otup[i][2]
        if len(otup[i]) == 4:
            df.Kingdom[i] = otup[i][0]
            df.Phylum[i] = otup[i][1]
            df.Class[i] = otup[i][2]
            df.Order[i] = otup[i][3]
        if len(otup[i]) == 5:
            df.Kingdom[i] = otup[i][0]
            df.Phylum[i] = otup[i][1]
            df.Class[i] = otup[i][2]
            df.Order[i] = otup[i][3]
            df.Family[i] = otup[i][4]
        if len(otup[i]) == 6:
            df.Kingdom[i] = otup[i][0]
            df.Phylum[i] = otup[i][1]
            df.Class[i] = otup[i][2]
            df.Order[i] = otup[i][3]
            df.Family[i] = otup[i][4]
            df.Genus[i] = otup[i][5]
        if len(otup[i]) == 7:
            df.Kingdom[i] = otup[i][0]
            df.Phylum[i] = otup[i][1]
            df.Class[i] = otup[i][2]
            df.Order[i] = otup[i][3]
            df.Family[i] = otup[i][4]
            df.Genus[i] = otup[i][5]
            df.Species[i] = otup[i][6]
    return df


# In[ ]:


def taxpreprocess_2(df):
    df = df.drop(df[df['t__'] == 0].index)
    df = df.drop(df[df['Metaphlan2_Analysis'] == 0].index)
    df = df.drop(df[df['OTU_ID'].str.contains('t__')].index)
    if 'taxonomy' in df.columns:
        df = df.drop('taxonomy', axis = 1)
    return df


# In[ ]:


for i in range(0, len(taxfiles)):
    df = pd.read_table(taxfiles[i])
    df_1 = taxpreprocess_1(df)
    df_2 = taxpreprocess_2(df_1)
    df_2["Visit_name"] = visitname[i]
    taxfiles[i] = df_2
    print("Completed", i+1, "/", len(taxfiles), "files.")


# Step 4/4: Merging the files & downloading the merged file(s):

# In[ ]:


for i in range(0, len(taxfiles)):
    Grouptaxfiles = pd.concat(taxfiles)


# In[ ]:


helperdf = pd.read_excel('helper.xlsx')
Grouptaxfiles = Grouptaxfiles.merge(helperdf)
#Name file as per folder
Grouptaxfiles.to_csv('UC_tax_processed.csv')

