import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

DEPENDENCIES = ["requests", "pyyaml", "prettytable", "clint", "toml"]


setuptools.setup(
    name="python-polyglot",  # Replace with your own username
    version="4.2.1",
    author="P Pranav Baburaj",
    author_email="code-roller@googlegroups.com",
    description=
    "Find the percentage of programming languages used in your project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pranavbaburaj/polyglot",
    packages=setuptools.find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=DEPENDENCIES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)