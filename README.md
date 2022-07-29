# Dissertation

## Data preparation
1. Load conda microbiome_env.yaml to make sure that all needed python libraries are available
2. Create 'Group<N>.xlsx' files based on the 9 groups mentioned in 'Master_List.xlsx'.
3. Run python script "prepare_biom_file_from_url.py". It has one parameter: excel file that has to have column "urls" containing urls for biom files to download

>python prepare_biom_file_from_url.py Group<N>.xlsx

3. Biom files are downloaded into the folder "data"
4. Biom files are convreted into tsv format and slightly modified to make them ready for neo4j loading.
5. Processed tsv files are in the folder "import_data"

## Data pre-processing
1. Run python script "Pathway_preprocessing.ipynb" on Jupyter.
2. Processed, merged excel files are downloaded per Group per category (pathway/enzyme/gene/taxon).

## Data loading
1. Load sample-level information from 'Master_List.xlsx' to create the following:

> nodes: Subject, Site, Visit number, Diagnosis, Sex, Race, Age &
> relationships: Subject -> Site, Visit num, Diagnosis, Sex, Race, Age

2. Load group-level information from each of the processed Excel files to create the following:

> nodes: Pathway/Enzyme/Gene/Taxon, Genus
> relationships: Subject -> Visit num -> Pathway/Enz/Gene/Taxon -> Genus
