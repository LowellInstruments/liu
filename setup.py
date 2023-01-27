from setuptools import setup, find_packages
import os


# export MY_INSTALL_REQUIRES_EMPTY=123 && pip install . -v
# -v allows to see 'print' statements

with open('requirements.txt') as f:
    rr = f.readlines()

if os.getenv('MY_INSTALL_REQUIRES_EMPTY') == '1':
    rr = []


setup(
    name='liu',
    version='1.0.2',
    packages=find_packages(),
    url='https://github.com/LowellInstruments/liu.git',
    license='MIT',
    author='kaz',
    install_requires=rr,
    author_email='',
    description='Package smaller than MAT lib with useful functions and data types'
)

