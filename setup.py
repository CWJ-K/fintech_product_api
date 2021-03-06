from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="api",  
    version="1.0.1", 
    description="invest product api",  
    long_description=long_description,  
    long_description_content_type="text/markdown",  
    keywords="finance, invest, python", 
)