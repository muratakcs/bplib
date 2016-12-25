#!/usr/bin/env python

from setuptools import setup

import bplib

setup(name='bplib',
      version=bplib.VERSION,
      description='A bilinear pairing library for petlib.',
      author='George Danezis',
      author_email='g.danezis@ucl.ac.uk',
      url=r'https://pypi.python.org/pypi/bplib/',
      packages=['bplib'],
      license="LGPL",
      long_description="""The bplib is a library implementing support for computations on groups supporting 
      bilinear pairings, as used in modern cryptography. 

      It provides python bindings to Diego Aranha's OpenPairing libraries, that use OpenSSL math 
      and crypto primitives. The bplibrary is an extension of petlib that provides easy to use 
      support for maths and ciphers used un modern Privacy Enhancing Technologies."

      """,

      setup_requires=["cffi>=1.0.0",
                      "pytest >= 2.6.4",
                      "petlib >= 0.0.30"],
      package_data = {
            "bplib": ["include/*.h"]},
      include_package_data = True,
      tests_require = [
            "cffi >= 1.0.0",
            "pycparser >= 2.10",
            "future >= 0.14.3",
            "pytest >= 2.5.0",
            "pytest-cov >= 1.8.1",
            "petlib >= 0.0.30"
            ],
      cffi_modules=["bplib/compile.py:_FFI"],
      install_requires=[
            "cffi >= 1.0.0",
            "pycparser >= 2.10",
            "future >= 0.14.3",
            "pytest >= 2.5.0",
            "pytest-cov >= 1.8.1",
            "msgpack-python >= 0.4.6",
            "petlib >= 0.0.30"
      ],
      zip_safe=False,
)