from setuptools import find_packages,setup 
#from typing import list


HYPE='-e .'

def get_requirements(file_path):

    requirements=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
        
        if HYPE in requirements:
            requirements.remove(HYPE)
    return requirements


setup(

name='mlproject',
version= '0.0.1',
author= 'Arjun',
author_email= 'arma.arjun97@gmail.com',
packages= find_packages(),
install_requires= get_requirements('requirements.txt')

)

