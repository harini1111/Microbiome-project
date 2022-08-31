#!/usr/bin/env python
# coding: utf-8

# Step 1: Importing necessary libraries:

# In[ ]:


import os
import pandas as pd
import re
import numpy as np


# Step 2: Loading all files from the Group:

# In[ ]:


#Use folder where the files to be processed are placed 
folder = r'C:/Users/Harini01.R/Desktop/Git/Microbiome-project/import_data/nonIBD'
files = os.listdir(folder)
ecsfiles = []


for file in files:
    if re.search(r"ecs", file):
        ecsfiles.append(f"{folder}/{file}")


# Step 3: Pre-processing the individual pathway files:

# In[ ]:


visitname = []
for file in ecsfiles:
    visitname.append(file[70:78])


# In[ ]:


otu = df.OTU_ID
otu = otu.astype(str).str.split('|')
otu[1][0].split(':')[0]


# In[ ]:


def enzpreprocess_1(df):
    if df.columns[1] != 'Abundance_RPKs':
        df.rename(columns = {df.columns[1] : 'Abundance_RPKs'}, inplace = True)
    otu = df.OTU_ID
    otu = otu.astype(str).str.split('|')
    df["Enzyme"] = ""
    df["Genus"] = ""
    for i in range (0,len(otu)):
        df.Enzyme[i] = otu[i][0].split(':')[0]
    for j in range(0,len(otu)):
        if(len(otu[j])<=1):
            df.Genus[j] = 0
        else:
            df.Genus[j] = otu[j][1].split('.')[0]
    return df


# In[ ]:


def enzpreprocess_2(df):
    df = df.drop(df[df['Genus'] == 0].index)
    df = df.drop(df[df['Genus'] == 'unclassified'].index)
    df = df.drop(df[df['Abundance_RPKs'] == 0].index)
    df = df.drop('OTU_ID', axis = 1)
    if 'taxonomy' in df.columns:
        df = df.drop('taxonomy', axis = 1)
    return df


# In[ ]:


for i in range(0, len(ecsfiles)):
    df = pd.read_table(ecsfiles[i])
    df_1 = enzpreprocess_1(df)
    df_2 = enzpreprocess_2(df_1)
    df_2["Visit_name"] = visitname[i]
    ecsfiles[i] = df_2
    print("Completed", i+1, "/", len(ecsfiles), "files.")


# Step 4: Merging the files & downloading the merged file(s):

# In[ ]:


for i in range(0, len(ecsfiles)):
    GroupAecsfiles = pd.concat(ecsfiles)


# In[ ]:


helperdf = pd.read_excel('diaghelper.xlsx')
GroupAecsfiles = GroupAecsfiles.merge(helperdf)
#Name file as per folder
GroupAecsfiles.to_csv('nonIBD_enz_processed.csv')

