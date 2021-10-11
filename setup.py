from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.1.0'
DESCRIPTION = 'A set of tools for Web Exploitation'
# LONG_DESCRIPTION = 'A package that (would) contains '

# Setting up
setup(
    name="webXtools",
    version=VERSION,
    author="Az3z3l (Yaswant)",
    author_email="<star7ricks@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["asyncio"],
    keywords=['python', 'hacking', 'ctf', 'web explotation', 'bruteforce'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)