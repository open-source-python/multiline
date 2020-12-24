from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="multiline",
    version="1.0.2",
    author="Sanket Tantia",
    author_email="tantiasanket@gmail.com",
    description="A package to read multline json values",
    long_description="""# multiline
Open source python module, which can parse multiline values in json files.
This module provides a wrapper on top of the four methods (load, loads, dump, dumps) present in the default json module. This is done to avoid the need of importing both modules `multiline` and `json`.

If multline parsing is required while loading the json, then an additional argument ```multiline=True``` needs to be provided to trigger the custom parser. More info on the package can be found at: https://sankettantia.medium.com/multiline-a-python-package-for-multi-line-json-values-c4f7a76f0305.
""",
    long_description_content_type="text/markdown",
    url="https://github.com/open-source-python/multiline.git", 
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)