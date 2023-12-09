from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    hyphen = '-e .'
    requirements = []
    with open(file_path, 'r') as f:
        requirements = [req.strip() for req in f.readlines()]
        requirements = [req for req in requirements if req != hyphen]
    return requirements

setup(
    name='ml project',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/Prasannajit123/ml_projects',
    license='MIT',
    author='prasannajit',
    author_email='prasannajitlenka504@gmail.com',
    description='necessary packages for ml projects',
    install_requires=get_requirements('requirement.txt')
    
)
