
# Set up environment
from sevenbridges import Api, Config
import os
from datetime import datetime
duration = 1  # seconds
freq = 440  # Hz
import sys

#set api
api=Api(config=Config(profile='default'))
api.aa = True

# Check for sys args
if len(sys.argv) == 5:
    path_name = sys.argv[1]
    folder_name = sys.argv[2]
    project_name = sys.argv[3]
    batch_name = sys.argv[4]
else:
    # Prompt user for inputs
    print("No command line arguments provided. Please enter the required information:\n")
    print("This Cavatica API download script requires 1. local download directory 2. New folder name 3. Cavatica project path 4. batch task ID\n")
    print("For further info see https://github.com/rob-fullem/excerpt_on_cavatica/tree/main\n")
    path_name = input("Enter the path to the existing local parent directory where new results sub folder with go: ")
    folder_name = input("Enter the sub folder name where files will be downloaded: ")
    project_name = input("Enter the Cavatica project id where batch task was run: ")
    batch_name = input("Enter the Cavatica batch task id: ")


#function to get all files
def list_all_files(files=None, project=None):
    if not files and not project:
        raise Exception(
            "Requires either a project object/id or list of file objects")
    if project and not files:
        files = api.files.query(project=project, limit=100, cont_token='init').all()
    file_list = []
    for file in files:
        if not file.is_folder():
            file_list.append(file)
        elif file.is_folder():
            child_nodes = file.list_files(limit=100, cont_token='init').all()
            file_list.extend(list_all_files(files=child_nodes))
    return file_list

# Get project info
#project = api.projects.get('eric_tobin/exrna-on-cavatica')
project = api.projects.get(project_name)

# Get batch task ID for study
batch_task_to_download = api.tasks.get(batch_name)

# Get children task for each sample in study from batch task
batch_task_to_download_list = list(batch_task_to_download.get_batch_children().all())

#add the study name to the path and mkdir
study_path = path_name + folder_name + "/"
if not os.path.exists(study_path):
    os.mkdir(study_path)
#loop through each sample task in study and get the output folder id and name. Create local folders if needed to download into
for t in batch_task_to_download_list:
    print("starting download at: ")
    print(datetime.now().time())
    print("task id ", t)
    for k, v in t.outputs.items():
        try:
            folder = api.files.get(v)
        except Exception as error:
            print("Can't locate output folder for task")
            print("Detected error: ", error)
            break
        sample_path = study_path + folder.name
        print(sample_path)
        #if skip_sample_string in folder.name:
        #    print("ser file: skipping")
        #    break
        if not os.path.exists(sample_path):
            os.mkdir(sample_path)
        files_to_download = list_all_files(files=[folder])
        for x in files_to_download:
            file_path = sample_path + '/' + x.name
            if not os.path.exists(file_path):
                download = x.download(file_path)












