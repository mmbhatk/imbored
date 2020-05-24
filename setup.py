from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="imbored",
    version="1.0.4",
    description="A Python package to display random facts, quotes and jokes.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/mmbhatk/imbored",
    author="Manasvi Bhat K",
    author_email="kmanasvibhat@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["imbored"],
    package_data={'imbored': ['data/*.json']},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "imbored = imbored.imbored:main",
        ]
    },
)