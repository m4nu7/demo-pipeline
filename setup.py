from setuptools import setup, find_packages

setup(name="census-income",
    version="0.0.1",
    author="Manohar",
    author_email="manohar.kot93@outlook.com",
    packages=find_packages(),
    install_requires=["pandas","numpy","flask"]
    )