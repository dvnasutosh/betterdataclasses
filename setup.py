from setuptools import find_packages, setup
import setuptools


setup(
    name="betterdataclass",
    version="3.01",
    description="A multipurpose dataclass libarary used for validation and data structuring.",
    long_description=open('./README.rst').read(),
    url='https://github.com/dvnasutosh/betterdataclasses',
    
    author="Asutosh Rath",
    author_email="dvnasutosh@gmail.com",
    packages=find_packages(),
    
    
        classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ]
)

'''
My directory setup
betterdataclasses(projectfolder)
--betterdataclass(libraryfolder)
----StrictDictionary.py
----StrictList.py
----__init__.py
----helper
------initiate.py
------validate.py
------to_dictr.py
'''