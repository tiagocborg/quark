# Setup file for package use_package_before_def

from setuptools import setup

setup(name="use_package_before_def",
      version="0.0.1",
      install_requires=["datawire-quark-core==0.4.1", "builtin==0.0.1"],
      packages=['test', 'use_package_before_def_md'])
