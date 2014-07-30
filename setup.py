__author__ = 'michogarcia'

from setuptools import setup, find_packages

version = '0.1'

setup(name='FullDiskAlert',
      version=version,
      author="Micho Garcia",
      author_email="micho.garcia@geomati.co",
      license="LICENSE.txt",
      description="Sends mail when disk is above threshold",
      packages=find_packages(),
      install_requires=[
          'pyyaml',
      ],
      )