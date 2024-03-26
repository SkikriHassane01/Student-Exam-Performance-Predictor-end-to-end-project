from setuptools import find_packages, setup

# this is is crucial for packaging Python projects.

# The `setup` function specifies the project's metadata and installation instructions, making it distributable and 
# installable via tools like pip.

# `find_packages` automates the inclusion of all project packages, ensuring completeness. Together, these components
# facilitate the easy sharing and installation of Python software, enhancing distribution and deployment processes.


setup(
    name="MLProject",
    version="0.0.1",
    author= "Hassane",
    author_email= "skikrihassane@gmail.com",
    packages= find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
    ]
)