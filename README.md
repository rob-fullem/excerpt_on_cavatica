# excerpt_on_cavatica
Instructions for using the ExceRpt RNA-Seq workflow on Cavatica cloud platform



https://docs.sevenbridges.com/docs/command-line-interface

## Download from Cavatica

Cavatica uses the Seven Bridges API to enable programmatic download of files to local systems. We recommend the python API client with instructions below.

**REQUIRED**: Must install python SB API libraries and enable authentication and configuration file. Learn more at https://sevenbridges-python.readthedocs.io/en/latest/quickstart.html

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
