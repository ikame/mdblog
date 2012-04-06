import os
import sys

from setuptools import setup, find_packages

py_version = sys.version_info[:2]

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, "README.txt")).read()
except IOError:
    README = ""

dependencies = [
    "distribute",
    "Pygments >= 1.5",
    "Markdown >= 2.1.1",
    "Jinja2 >= 2.6"
]

scripts = {
    "console_scripts": [
        "mdblog-init = mdblog.scripts.init:main",
        "mdblog-serve = mdblog.scripts.serve:main",
        "mdblog-build = mdblog.scripts.build:main"
    ]
}


setup(name="mdblog",
      version="1.0",
      description="Static blog generator",
      long_description=README,
      author="Anler Hernandez Peral",
      author_email="anler86@gmail.com",
      url="http://github.com/ikame/mdblog/",
      license="MIT",
      packages=find_packages(exclude=["tests"]),
      entry_points=scripts,
      test_suite="mdblog.tests",
      install_requires=dependencies,
      keywords="weblog blog journal diary atom",
      classifiers=[
          "Environment :: Console",
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "Operating System :: POSIX",
          "Topic :: Software Development :: Blog Website"])
