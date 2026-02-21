from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    Docstring for get_requirements
    
    :return: Description
    :rtype: List[str]
    this will get a list of requirements
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt',"r") as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()

                if requirement and requirement!= "-e . ": #dont add this
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("File not found")

    return requirement_list

print(get_requirements())