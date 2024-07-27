from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function returns a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements] #/n will also be added while reading lines, hence replacing wth blanks

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # removing -e. from requirements list   

    return requirements 


setup(
    name='mlproject',
    version='0.0.1',
    author='Areesha',
    author_email='areeshaanjum748@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)