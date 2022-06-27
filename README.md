# Dissertation

## Data preparation
1. Load conda microbiome_env.yaml to make sure that all needed python libraries are available
2. Run python script "prepare_biom_file_from_url.py". It has one parameter: excel file that has to have column "urls" containing urls for biom files to download

>python prepare_biom_file_from_url.py IBD_samples_files_test.xlsx

3. Biom files are downloaded into the folder "data"
4. Biom files are convreted into tsv format and slightly modified to make them ready for neo4j loading.
5. Processed tsv files are in the folder "import_data"