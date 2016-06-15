from setuptools import setup, find_packages

from airship_convert import __author__, __version__

setup(
    name="airship_convert",
    version=__version__,
    packages=find_packages("."),
    url="",
    license="MIT",
    author=__author__,
    author_email="",
    description="",
    install_requires=["jinja2", "pypandoc"],
    scripts=["bin/airship-convert"],
    package_data={"": ["templates/markdown/*"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
)
