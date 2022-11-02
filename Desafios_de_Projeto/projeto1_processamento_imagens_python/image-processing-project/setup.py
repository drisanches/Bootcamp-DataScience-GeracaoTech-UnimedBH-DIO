from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Image_processing",
    version="0.0.2",
    author="Drielly",    
    description="Image Processing Package using Skimage", 
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drisanches/Bootcamp-DataScience-GeracaoTech-UnimedBH-DIO.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)