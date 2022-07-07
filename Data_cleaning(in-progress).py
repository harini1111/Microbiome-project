#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
os.getcwd()
os.chdir('C:/Users/Harini01.R/Desktop/Git/Microbiome-project/import_data')


# In[2]:


df1 = pd.read_table("MSM5LLDA_taxonomic_profile.biom.tsv")


# In[3]:


def cleaning(df):
    df["helper"] = " "
    OTUIDs = df.OTU_ID
    OTUIDs = OTUIDs.str.split('|')
    for i in range(0,len(OTUIDs)):
        for j in range(0,len(OTUIDs[i])):
            if(OTUIDs[i][j][:2] == 's_'):
                df.helper[i] = 1 
    for k in range(0,len(OTUIDs)):
        for l in range(0,len(OTUIDs[k])):
            if(OTUIDs[k][l][:2] == 't_'):
                df.helper[i] = 2  
    df_s = df[df['helper'] == 1]
    del df_s['helper']
    del df_s['taxonomy']
    df_s
    return df_s


# In[4]:


df1c = cleaning(df1)
df1c


# Cells below are in progress; the following is what I'm trying to do:
# - Extract only 's__' names from 'OTU_ID'
# - Replace 'Metaphlan Analysis2' as the sample name ('MSM5LLDA' here) from file name
# - Be able to append Abundances from multiple files on the right side of existing dataframe


# In[ ]:


df1 = df.sort_values(by=['MSM5LLDI_Abundance'], ascending=[False])
df1
print(df1)



# In[ ]:


d = 'k__Bacteria|p__Firmicutes|c__Clostridia|o__Clostridiales|f__Clostridiales_noname|g__Pseudoflavonifractor|s__Pseudoflavonifractor_capillosus'
x = d.split("|")
print(x)


# In[ ]:


for i in range(0,len(df1)):
    test.append(df1.OTU_ID[i].split('|'))
    if test[i].str.contains()
df1s = df1[df1["OTU_ID"].str.contains("s__")]
df1['splits'] = test
df1.splits[3]
df = df1.merge(df2, how='outer')
print(df)
df_left = df1.merge(df2, how='inner')
print(df_left)
df_join = df1.set_index('OTU_ID').join(df2.set_index('OTU_ID'), lsuffix='_l', rsuffix='_r')
print(df_join)
df_join.head(10)
df_join.index[0]
for i in range(0,len(df_join)):
    if df1[0:i].OTU_ID == 's__':
        df1[['OTU_ID', 'species']] = df1['OTU_ID'].str.split('|s__', 1, expand=True)

