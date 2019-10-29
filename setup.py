import pathlib
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

# This call to setup() does all the work
setup(
    name="temporal_dimension",
    version='0.1.0',
    description="Processing temporal dimension with python",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    url='https://github.com/kamranhossain/temporal_dimension',
    author="Kamran Hossain",
    author_email='kamran.hossain22@yahoo.com',
    license="MIT license",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=['temporal_dimension'],
    include_package_data=True,
    install_requires=requirements,
    keywords='temporal_dimension',
    zip_safe=False,
)

