from setuptools import setup
from setuptools import find_packages

setup(
    name="decisionlab",
    version="0.0.1",
    packages=find_packages(),
    author="decisionLab",
    author_email="jsanchezcastillejos@gmail.com",
    description="A Python package for accessing decision data from JustDecision.com",
    url="https://github.com/TuDecides/decisionlab",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
