from setuptools import setup, find_packages

from typing import List


PROJECT_NAME = "Machine Learning"
VERSION = "0.0.1"
DESCRIPTION = " This is MY Machine Learning project in Moduler Coding"
AUTHOR_NAME ="Arif"
AUTHOR_EMAIL = 'kamruzzaman.sust15@gmail.com'


REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ." 

def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirements_files:
        requirements_list =  requirements_files.readlines()
        requirements_list = [requirement_name.replace("\n","")for requirement_name in requirements_list ]
        

        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)
        


setup (
    name =PROJECT_NAME,
    version =VERSION ,
    description= DESCRIPTION,
    author =AUTHOR_NAME ,
    author_email = AUTHOR_EMAIL,
    #url = 'https://www.python.org/sigs/distutils-sig/',
    packages=find_packages() ,
    install_requires = get_requirements_list()
)

