"""
This is the setup script for the 'inked' package.
The 'inked' package is a tool for adding text or image watermarks to images.
Attributes:
    name (str): The name of the package.
    version (str): The current version of the package.
    packages (list): A list of all Python import packages that should be
    included in the distribution package.
    install_requires (list): A list of packages that are required for this package to work.
    entry_points (dict): A dictionary of entry points, specifying what scripts should be
    made available to the command line.
    author (str): The name of the author of the package.
    author_email (str): The email address of the author.
    description (str): A short description of the package.
    long_description (str): A long description of the package, read from the README.md file.
    long_description_content_type (str): The format of the long description.
    url (str): The URL for the package's homepage.
    classifiers (list): A list of classifiers that describe the package.
    python_requires (str): The Python version required for the package.
"""
from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="inked",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        "Pillow>=8.0.0"
    ],
    entry_points={
        "console_scripts": [
            "add-watermark = inked.watermark:main",
        ],
    },
    author="Sumesh.K",
    author_email="ksumesh21@gmail.com",
    description="A tool for adding text or image watermarks to images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ksumesh21/inked",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
