# Setup file for package constructors

from setuptools import setup

setup(name="constructors",
      version="0.0.1",
      install_requires=["datawire-quark-core==0.4.1", "builtin==0.0.1"],
      packages=['test1', 'test2', 'test3', 'constructors_md'])
