from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = 'e .'


def get_requirements(file_path: str) -> List[str]:
    """
    this function takes a file_path of required packages
    :param file_path: requirements.txt
    """

    with open(file_path) as file_name:
        requirements = file_name.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        requirements.pop()
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Gil Linenberg',
    author_email='g.linenberg@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
