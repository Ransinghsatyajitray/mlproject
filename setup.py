from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_paths:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_paths) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # in the setup.py we are installing just the packages and not the set up.py so we are removing -e . which is also a package
    return requirements        


setup(
    name='mlproject',
    version='0.0.1',
    author='Ransingh',
    author_email = 'satyajit239@gmail.com',
    packages=find_packages(),
    install_requires=  get_requirements('requirements.txt')     #  ['pandas','numpy', 'seaborn'] wrong approach to mention explicitly as we may require 100s of packages 
)
