from setuptools import setup

from whych import __version__

with open('README.rst', 'r') as f:
    readme = f.read()

setup(name="whych",
      version=__version__,
      description="A module to find modules",
      long_description=readme,
      author="Pierre de Buyl",
      author_email="pdebuyl@pdebuyl.be",
      license="BSD",
      url="https://github.com/pdebuyl/whych",
      packages=["whych"],
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities',
      ],
      )
