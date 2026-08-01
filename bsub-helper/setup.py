from setuptools import setup
from setuptools import find_packages

setup(name='bsub-helper',
      version='0.1',
      description='custom helper to submit bsub files',
      url='http://github.com/gwaygenomics/bsub-helper',
      author='Gregory Way',
      author_email='gregory.way@gmail.com',
      license='MIT',
      packages=find_packages(),
      python_requires='>=3.4')
