# Microbiome Knowledge Graph

Knowledge graphs are increasingly being used to capture biological data due to its adaptability towards inter-related datasets, flexibility, and ability to handle large amounts of data. One of the key areas of application of knowledge graphs is in microbiome data analysis since microbiome data is usually generated in massive amounts. In order to explore the construction of microbiome knowledge graphs, we use data from the Inflammatory Bowel Disease (IBD) study done as part of the Human Microbiome Project (Phase 2).  IBD, a chronic inflammatory disease of the human gut, is a growing cause for concern in Europe. Characterized by symptoms such as ulcers, diarrhea and gut inflammations, a key factor known to be majorly affected in IBD patients is the diversity in gut microbiota. There is substantial evidence that few bacterial families are present in highly different proportions between healthy and IBD patient samples. This variation in microbial populations could be linked to differential interaction between the microbiota and mucosal immune system, causing dysbiosis. Here, we have explored the relationships between bacterial families and their involvement in few pathways & enzymes in healthy and IBD cohorts based on differential abundances. We have built a knowledge graph linking taxonomical and functional factors to visualize and analyze the diversity of bacterial families & expression of pathways and enzymes in between cohorts. Abundance matrix tables were extracted, pre-processed and loaded onto Neo4j for pathway, enzyme and taxonomical abundances. The knowledge graph was then explored along the following lines:
1. Microbial diversity among cohorts
2. Microbial diversity among cohorts stratified by metadata
3. Microbial expression profile for pathways
4. Enzyme expression in most abundant pathway
5. Enzyme expression in butyrate production pathway

## Data Source: 
The Human Microbiome Project, and specifically the IBD cohort was selected. Abundance matrix files were downloaded from https://portal.hmpdacc.org/.

## Data Model: 
An Entity-Relationship model was constructed as below:
![image](https://user-images.githubusercontent.com/93226452/187973567-80740fe7-6e84-40a7-a631-8c73788e90ce.png)

## Data Extraction & Pre-processing:
Since abundance matrix files were present in .biom format, they were converted to .tsv format. To pre-process them to make them suitable for loading onto Neo4j, python scripts were written.

## Knowledge Graph:
The final schema of the KG built on Neo4j looked like:
![image](https://user-images.githubusercontent.com/93226452/187973934-237f8110-a63e-48a2-9bc2-d1cbfb1f9427.png)

For more information on any of the above steps, please contact myself (hariniraghavan96@gmail.com) or Natalja Kurbatova (natalja.kurbatova@zifornd.com) from Zifo RnD Solutions.
