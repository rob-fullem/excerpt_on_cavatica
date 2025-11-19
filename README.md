# excerpt_on_cavatica
Instructions for using the ExceRpt RNA-Seq workflow on Cavatica cloud platform. Temporarily this is only for existing users in cavatica workspace. Public workspace and pipelines are in progress.

## Upload to Cavatica

For upload of large amounts of fastq data it is highly recommended you use the Seven Bridges CLI. Learn more at https://docs.cavatica.org/docs/upload-via-the-command-line

## Running excerpt on Cavatica

Three versions currently exist of the excerpt to bedgraph pipeline. The core version - https://cavatica.sbgenomics.com/u/rlfullem/excerpt-processing/apps/excerpt2bedgraphpipelinev4_1/1

An alternative version for when fastq files have spike in oligos for calibration (requires providing a bowtie archive of reference oligos): https://cavatica.sbgenomics.com/u/rlfullem/excerpt-processing/apps/excerpt2bedgraphpipelinev4spikealt/3

An alternative version for when fastq files end in .fq rather than .fastq: https://cavatica.sbgenomics.com/u/rlfullem/excerpt-processing/apps/excerpt2bedgraphpipelinevfqalt/1

Eventually, all versions will be merged into one pipeline that more gracefully handles edge cases but this is currently in progress. All pipelines default to 1 mismatch allowed in aligning reads. If you wish to restrict this parameter to 0 then you must define that in the app settings when running your tasks. 


## Download from Cavatica

Cavatica uses the Seven Bridges API to enable programmatic download of files to local systems. We recommend the python API client with instructions below.

**REQUIRED**: Must install python SB API libraries and enable authentication and configuration file. Learn more at https://sevenbridges-python.readthedocs.io/en/latest/quickstart.html

**BEFORE DOWNLOADING BULK SETS OF FILES**: It is highly recommended you delete any temp or intermediate files that are generated during excerpt runs. These may be large files and significantly slow your downloads and increase storage requirements.

List of files often preferable to delete before using download script:



**cavatica_api_download.py manual**
Four arguments required. Can be provided as sys arguments or interactively at runtime
Usage: 
`python cavatica_api_download.py <parent_local_folder_path> <new_results_folder_name> <Project_name_on_Cavatica> <Batch_Task_ID>`

**Args explained:**

Project_name_on_Cavatica and Batch_Task_ID can both be found in the url of any batch task job on Cavatica

Project_name_on_Cavatica: The project name is the project id and project creater name. Appears in URL after `https://cavatica.sbgenomics.com/u/` and before `/tasks/`

Batch_Task_ID: The batch task id is the alphanumeric id in the url following `/tasks/`. The id ends at the next backslash "/"

![Image of where to retrieve download ids from URL on Cavatica](https://github.com/rob-fullem/excerpt_on_cavatica/blob/main/sys_vars_image.svg)

**Example:** 
python cavatica_api_download.py /PATH/TO/EXISTING/PARENT/DIRECTORY/FOR/DOWNLOADs/ NEW_DOWNLOAD_TEST rlfullem/exrna-otherbiofluids a046934a-80ba-472c-ae13-7592b30d5541
