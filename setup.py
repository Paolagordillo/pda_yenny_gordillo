
from setuptools import setup, find_packages

setup(
    name= "pad",
    version="0.0.1",
    author="Paola Gordillo",
    author_email="yenny.gordillo@est.iudigital.edu.co",
    description="configuracion pad",
    py_modules=["actividad_1"],
    install_requires=[
          "kagglehub[pandas-datasets]>=0.3.8",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.2",
        "pandas",
        "numpy",
        "openpyxl",
        "requests",
        "scipy"
        
    ],
    
)
