# Setup file for package multiple_packages

from setuptools import setup

setup(name="multiple_packages",
      version="0.0.1",
      install_requires=["builtin==0.0.1"],
      py_modules=['multiple_packages'],
      packages=['p1', 'p1.p2', 'multiple_packages_md'])