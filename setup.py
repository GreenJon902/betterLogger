import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="betterLogger",
    version="1.6",
    description="A great colored logger!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/GreenJon902/betterLogger",
    author="GreenJon",
    author_email="GreenJon902@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9"
    ],
    packages=["betterLogger"],
    include_package_data=True,
    install_requires=["appdirs"],
    entry_points={
        "console_scripts": [
            "betterLogger=betterLogger.__init__:main",
        ]
    },
)
