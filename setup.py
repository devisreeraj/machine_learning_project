from setuptools import setup,find_packages
from typing import List



#DECLARING VARIABLES FOR SETUP FUNCTIONS
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.3"
AUTHOR = "Devisree Raj"
DESCRIPTION = "This is a first FSDS Nov batch Machine Learning Project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_lists()->List[str]:
        #"""
        #Description: This function is going to return list of requirement
        #mention in requirements.txt file

        #return: This function is going to return a list which contain name of libraries mentioned in requirements.txt file
        #"""
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),  #PACKAGES,
    install_requires = get_requirements_lists()
)


