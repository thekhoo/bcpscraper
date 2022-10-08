from pathlib import Path
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.2'
DESCRIPTION = "Blackstone's Criminal Practice 2022 PDF Scraper"
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="bcpscraper",
    version=VERSION,
    author="Christopher Khoo Jinn Wei",
    author_email="<khoojinnwei@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['docx','lxml','Pillow','PyPDF2','typing_extensions','python-docx','regex'],
    keywords=['python',"Blackstone's Criminal Practice 2022",'law','law document','lexisnexis','lexislibrary'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Legal Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Education"
    ]
)