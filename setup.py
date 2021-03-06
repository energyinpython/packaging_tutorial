import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-package-energyinpython",
    version="0.0.7",
    author="Energy in Python",
    author_email="rubinn2@wp.pl",
    description="A package for preferences identification and MCDM evaluation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/energyinpython/packaging_tutorial",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)