__author__ = 'michogarcia'

from setuptools import setup, find_packages

version = '0.1'

setup(name='FullDiskAlert',
      version=version,
      author="Micho García",
      author_email="micho.garcia@geomati.co",
      license="GPLv3",
      description="Sends mail when disk is above threshold",
      packages=find_packages(),
      install_requires=[
          'pyyaml',
      ],
      )