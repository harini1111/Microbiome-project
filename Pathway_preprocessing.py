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


# Step 3: Pre-processing the individual files:

# In[ ]:


visitname = []
for file in pwyfiles:
    visitname.append(file[70:78])


# In[ ]:


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


# In[ ]:


def pwypreprocess_2(df):
    df = df.drop(df[df['Genus'] == 0].index)
    df = df.drop(df[df['Genus'] == 'unclassified'].index)
    df = df.drop(df[df['Abundance'] == 0].index)
    df = df.drop('OTU_ID', axis = 1)
    if 'taxonomy' in df.columns:
        df = df.drop('taxonomy', axis = 1)
    return df


# In[ ]:


for i in range(0, len(pwyfiles)):
    df = pd.read_table(pwyfiles[i])
    df_1 = pwypreprocess_1(df)
    df_2 = pwypreprocess_2(df_1)
    df_2["Visit_name"] = visitname[i]
    pwyfiles[i] = df_2
    print("Completed", i+1, "/", len(pwyfiles), "files.")


# Step 4: Merging the files & downloading the merged file(s):

# In[ ]:


for i in range(0, len(pwyfiles)):
    Grouppwyfiles = pd.concat(pwyfiles)


# In[ ]:


helperdf = pd.read_excel('helper.xlsx')
Grouppwyfiles = Grouppwyfiles.merge(helperdf)
#Name file as per folder
Grouppwyfiles.to_csv('nonIBD_processed.csv')

