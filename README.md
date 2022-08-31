# Dissertation

## Data extraction
1. Launch https://portal.hmpdacc.org/. 
2. For 'Get Started By Exploring' button, select 'Data'.
3. From the filters on the left side, select the following:
Projects: Integrative Human Microbiome Project
Body Site: feces
Studies: IBDMDB
4. From the pie chart for 'File Counts by File Type', select 'abundance_matrix'  in the pie chart.
5. Navigate to the 'Files' tab and add all files to cart. 
6. Move to the cart and download both 'File Manifest' as well as 'Sample Metadata'.
7. For the two files, 'sample_id' is a common field. Using this, merge the two files to create one single Excel file.

<>


## Data preparation
1. Load conda microbiome_env.yaml to make sure that all needed python libraries are available
2. Create 'Group<N>.xlsx' files based on the 9 groups mentioned in 'Master_List.xlsx'. (Groups are only created to process large amount of files in smaller steps. This step can be omitted if step 3 can be run for all the files to be downloaded, if processing capacity is adequate.)
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
