from setuptools import setup, find_packages
#from setuptools.command.develop import develop
#from setuptools.command.install import install

setup(
        name="QSDCalcs",
        version="0.1.4",
        packages=find_packages(exclude=['*test']),
        author="Gareth Sion Jones",
        author_email="garethsion@googlemail.com",
        project_urls={
            'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
            'Source': 'https://github.com/garethsion/SpecialResonatorCalcs.git',
            },
        install_requires=['numpy','scipy']
    )