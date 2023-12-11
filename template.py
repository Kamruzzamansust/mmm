# import os , sys 

# from pathlib import Path 

# import logging 

# while True:
#     project_name = input('Enter Your project Name:')

#     if project_name !="":
#         break

#     list_of_files =[
#         f"{project_name}/__init__.py",
#         f"{project_name}/components/__init__.py",
#         f"{project_name}/config/__init__.py",
#         f"{project_name}/constants/__init__.py",
#         f"{project_name}/entity/__init__.py",
#         f"{project_name}/exception/__init__.py",
#         f"{project_name}/logger/__init__.py",
#         f"{project_name}/pipeline/__init__.py",
#         f"{project_name}/utils/__init__.py",
#         f"config/config.yaml",
#         "schema.yaml",
#         "app.py",
#         "main.py",
#         "logs.py",
#         "exception.py",
#         "setup.py",
#     ]

#     for  filepath in list_of_files:
#         filepath = Path(filepath)
#         filedir, filename = os.path.split(filepath)

#         if filedir !="":
#             os.makedirs(filedir,exist_ok=True)

#         if (not os.path.exists(filepath)) or(os.path.getsize(filepath)==0):
#             with open(filepath,"w") as f:
#                 pass
#         else:
#             logging.info("file is already at: {filepath}")

    
import os
import logging
from pathlib import Path

while True:
    project_name = input('Enter Your project Name:')

    if project_name != "":
        break

base_directory = Path(project_name)

# Create the 'src' directory
src_directory = base_directory / 'src'
os.makedirs(src_directory, exist_ok=True)

list_of_files = [
    f"{src_directory}/__init__.py",
    f"{src_directory}/components/__init__.py",
    f"{src_directory}/config/__init__.py",
    f"{src_directory}/constants/__init__.py",
    f"{src_directory}/entity/__init__.py",
    f"{src_directory}/exception/__init__.py",
    f"{src_directory}/logger/__init__.py",
    f"{src_directory}/pipeline/__init__.py",
    f"{src_directory}/utils/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = filepath.parent, filepath.name

    os.makedirs(filedir, exist_ok=True)

    if not filepath.exists() or os.path.getsize(filepath) == 0:
        with open(filepath, "w"):
            pass
    else:
        logging.info(f"File already exists at: {filepath}")

   
    

    
