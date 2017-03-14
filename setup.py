from setuptools import setup

from whych import __version__

setup(name="whych",
      version=__version__,
      description="Find the location for a given module",
      author="Pierre de Buyl",
      author_email="pdebuyl at pdebuyl dot be",
      license="BSD",
      url="https://github.com/pdebuyl/whych",
      packages=["whych"],
      )
