#!/usr/bin/env python
import re, os, glob
try:
    from setuptools import setup, Extension, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, Extension, find_packages

# Following the recommendations of PEP 396 we parse the version number
# out of the module.
def parse_version(module_file):
    f = open(module_file)
    s = f.read()
    f.close()
    match = re.findall("__version__ = '([^']+)'", s)
    return match[0]

f = open(os.path.join(os.path.dirname(__file__), "README.md"))
err_readme = f.read()
f.close()

setup(
    name="err",
    version=parse_version(os.path.join("err", "__init__.py")),
    description="A library to standardize HTTP errors",
    long_description=err_readme,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    author='Vasyl Yovdiy',
    author_email='yovdiyvasyl@gmail.com',
    url="https://github.com/y-vas/status-handlers",
    python_requires='>=3.7',  # Your supported Python ranges
    keywords=[
        "err",
        "status",
        "handler",
    ],
    license="GNU",
    classifiers=[
        "Topic :: Utilities",
    ],
    install_requires=[
    ],
)
