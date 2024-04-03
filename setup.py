import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iv_params",
    version="0.0.6",
    author="Michael Deceglie",
    author_email="michael.deceglie@nrel.gov",
    description="Perform ASTM E1036 extraction of photovoltaic IV parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NREL/iv_params",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['pandas', 'numpy', 'matplotlib']
)
