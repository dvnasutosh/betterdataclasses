from setuptools import setup
f=open("./README.md",'r')
readme=f.readlines()

setup(
    name="betterdataclass",
    version="2.02",
    description="A multipurpose dataclass libarary used for validation and data structuring.",
    long_description="\n".join(readme),
    url='https://github.com/dvnasutosh/betterdataclasses',
    
    author="Asutosh Rath",
    author_email="dvnasutosh@gmail.com",
    packages=['betterdataclass','betterdataclass.helper'],
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